"""Browser acceptance checks for the generated local teaching resource."""
from pathlib import Path
import json
import re
from playwright.sync_api import sync_playwright
import fitz

ROOT = Path(__file__).resolve().parent
QA = ROOT / 'qa'
QA.mkdir(exist_ok=True)
data = json.loads((ROOT/'quiz-data.json').read_text(encoding='utf-8'))
checks=[]
def ok(name,condition):
 assert condition,name
 checks.append(name)
 print('PASS:',name,flush=True)

with sync_playwright() as p:
 browser=p.chromium.launch(headless=True,executable_path=r'C:\Users\onyei\.cache\puppeteer\chrome\win64-146.0.7680.76\chrome-win64\chrome.exe')
 page=browser.new_page(viewport={'width':1440,'height':1000})
 errors=[]
 page.on('pageerror',lambda e: errors.append(str(e)))
 page.goto((ROOT/'index.html').as_uri())
 ok('28 slides rendered',page.locator('.slide').count()==28)
 ok('Only first slide initially visible',page.locator('.slide:visible').count()==1 and page.locator('#slide-1').is_visible())
 ok('Back disabled at start',page.locator('#previous').is_disabled())
 page.screenshot(path=str(QA/'deck-desktop.png'),full_page=True)
 page.keyboard.press('ArrowRight')
 ok('Keyboard and hash navigation',page.locator('#slide-2').is_visible() and page.url.endswith('#slide-2'))
 page.locator('#jump').select_option('7')
 page.locator('#rvu').fill('5')
 page.locator('#work').fill('3')
 ok('Independent calculator formulas',page.locator('#payment').inner_text()=='$167.00' and page.locator('#pay').inner_text()=='$165.00')
 page.locator('#rvu').fill('-1')
 ok('Invalid calculator input handled','valid' in page.locator('#payment').inner_text())
 page.locator('#rvu').fill('4')
 page.locator('#work').fill('2')
 page.locator('#refs-open').click()
 ok('References dialog opens',page.locator('#reference-panel').is_visible())
 page.keyboard.press('Escape')
 ok('Escape closes references',not page.locator('#reference-panel').is_visible())
 for width,height in [(1440,1000),(390,844),(320,740)]:
  page.set_viewport_size({'width':width,'height':height})
  for n in range(1,29):
   page.locator('#jump').select_option(str(n))
   overflow=page.evaluate('document.documentElement.scrollWidth > innerWidth+1')
   assert not overflow,f'Horizontal overflow slide {n} width {width}'
  ok(f'All 28 slides fit horizontally at {width}px',True)
 page.set_viewport_size({'width':390,'height':844})
 page.locator('#jump').select_option('20')
 page.screenshot(path=str(QA/'deck-mobile.png'),full_page=True)
 page.locator('#jump').select_option('23')
 page.locator('#slide-23 summary').click()
 ok('Case answer reveals',page.locator('#slide-23 details').get_attribute('open') is not None)
 page.locator('#jump').select_option('28')
 ok('Next disabled at end',page.locator('#next').is_disabled())
 page.locator('#jump').select_option('1')
 page.locator('#slide-1 h1').focus()
 page.keyboard.press('End')
 ok('End key goes to references',page.locator('#slide-28').is_visible())
 page.keyboard.press('Home')
 ok('Home key returns to title',page.locator('#slide-1').is_visible())
 # Print uses the same document, including expanded case answers.
 page.set_viewport_size({'width':1440,'height':1000})
 page.pdf(path=str(ROOT/'presentation.pdf'),prefer_css_page_size=True,print_background=True)
 doc=fitz.open(ROOT/'presentation.pdf')
 ok('Presentation PDF has exactly 28 pages',len(doc)==28)
 for n in [0,6,19,27]:
  doc[n].get_pixmap(matrix=fitz.Matrix(1,1)).save(QA/f'pdf-slide-{n+1}.png')
 ok('All PDF slide numbers survive',all(re.search(rf'{n+1:02}\s*/\s*28',doc[n].get_text()) for n in range(28)))
 doc.close()
 for track,count in [('physician',12),('app',12),('all',16)]:
  page.goto((ROOT/'quiz.html').as_uri()+'?track='+track)
  pool=[q for q in data if q['track']=='shared' or track=='all' or q['track']==track]
  ok(track+' track question count',len(pool)==count and page.locator('#question-count').inner_text()==f'1 / {count}')
  ok(track+' requires answer before submission',page.locator('#submit').is_disabled())
  for n,q in enumerate(pool):
   ok(f'{track} question {q["id"]} order',page.locator('#question-title').inner_text()==q['question'])
   page.locator(f'input[value="{q["correct"]}"]').check()
   page.locator('#submit').click()
   assert page.locator('#feedback h2').inner_text()=='Correct'
   assert page.locator('.rationales li').count()==4
   assert page.locator('input[name=answer]:disabled').count()==4
   page.locator('#advance').click()
  ok(track+' perfect score',f'{count} / {count}' in page.locator('#results .metric').inner_text())
  ok(track+' perfect attempt disables retry',page.locator('#retry').is_disabled())
  page.locator('#restart').click()
  ok(track+' restart resets progress',page.locator('#question-count').inner_text()==f'1 / {count}' and page.locator('#quiz-progress').get_attribute('value')=='0')
 # All incorrect checks scoring, per-domain accounting, and retry subset.
 page.goto((ROOT/'quiz.html').as_uri()+'?track=all')
 for q in data:
  page.locator(f'input[value="{(q["correct"]+1)%4}"]').check()
  page.locator('#submit').click()
  assert page.locator('#feedback h2').inner_text()=='Review this decision'
  page.locator('#advance').click()
 ok('All-wrong score is zero','0 / 16' in page.locator('#results .metric').inner_text())
 ok('Per-domain denominators total 16',sum(int(t.split('/')[1]) for t in page.locator('.domain-grid b').all_inner_texts())==16)
 page.screenshot(path=str(QA/'quiz-results.png'),full_page=True)
 page.locator('#retry').click()
 ok('Retry identified as practice','Missed-question practice' in page.locator('#track-label').inner_text())
 page.locator('#change-track').click()
 ok('Track selection restores choices',page.locator('#setup').is_visible() and not page.locator('#quiz').is_visible())
 # One missed question must yield a one-question retry.
 page.locator('[data-track=app]').click()
 pool=[q for q in data if q['track'] in ['shared','app']]
 for i,q in enumerate(pool):
  answer=(q['correct']+1)%4 if i==0 else q['correct']
  page.locator(f'input[value="{answer}"]').check();page.locator('#submit').click();page.locator('#advance').click()
 ok('Mixed score is 11 of 12','11 / 12' in page.locator('#results .metric').inner_text())
 page.locator('#retry').click()
 ok('Retry contains only missed question',page.locator('#question-count').inner_text()=='1 / 1')
 page.locator(f'input[value="{pool[0]["correct"]}"]').check();page.locator('#submit').click();page.locator('#advance').click()
 ok('Retry score is separate and correct','1 / 1' in page.locator('#results .metric').inner_text() and 'practice result' in page.locator('#results').inner_text().lower())
 page.set_viewport_size({'width':390,'height':844})
 page.goto((ROOT/'quiz.html').as_uri())
 page.screenshot(path=str(QA/'quiz-mobile.png'),full_page=True)
 page.locator('[data-track=app]').click()
 for q in pool:
  page.locator(f'input[value="{q["correct"]}"]').check();page.locator('#submit').click()
  assert not page.evaluate('document.documentElement.scrollWidth > innerWidth+1'),q['id']
  if q['id']=='A3':page.screenshot(path=str(QA/'feedback-mobile.png'),full_page=True)
  page.locator('#advance').click()
 ok('Mobile quiz questions and feedback fit',True)
 # Keyboard selection and swipe interaction.
 page.goto((ROOT/'quiz.html').as_uri()+'?track=physician')
 page.locator('input[name=answer]').first.focus()
 page.keyboard.press('ArrowDown')
 ok('Native keyboard radio selection',page.locator('input[name=answer]:checked').count()==1)
 page.goto((ROOT/'index.html').as_uri())
 page.evaluate('''() => {const el=document.querySelector('main');
 const a=new Touch({identifier:1,target:el,clientX:300,clientY:300});
 const b=new Touch({identifier:1,target:el,clientX:100,clientY:310});
 el.dispatchEvent(new TouchEvent('touchstart',{bubbles:true,touches:[a]}));
 el.dispatchEvent(new TouchEvent('touchend',{bubbles:true,changedTouches:[b]}));}''')
 page.wait_for_function('location.hash==="#slide-2"')
 ok('Horizontal touch swipe advances',page.locator('#slide-2').is_visible())
 page.goto((ROOT/'answer-key.html').as_uri())
 ok('Answer key has all 16 cases',page.locator('.key-question').count()==16)
 page.pdf(path=str(ROOT/'answer-key.pdf'),prefer_css_page_size=True,print_background=True)
 key=fitz.open(ROOT/'answer-key.pdf')
 ok('Answer key PDF includes all case IDs',all(q['id'] in re.sub(r'\s+', '', ''.join(x.get_text() for x in key)) for q in data))
 key[1].get_pixmap(matrix=fitz.Matrix(1,1)).save(QA/'pdf-answer-key.png')
 key.close()
 ok('No browser JavaScript errors',not errors)
 browser.close()
 # Standalone pages also remain readable without scripting.
 browser=p.chromium.launch(headless=True,executable_path=r'C:\Users\onyei\.cache\puppeteer\chrome\win64-146.0.7680.76\chrome-win64\chrome.exe')
 nojs=browser.new_page(java_script_enabled=False)
 nojs.goto((ROOT/'index.html').as_uri())
 ok('No-JavaScript deck exposes all slides',nojs.locator('.slide:visible').count()==28)
 browser.close()
(QA/'results.json').write_text(json.dumps({'passed':len(checks),'checks':checks,'javascript_errors':errors},indent=2),encoding='utf-8')
print('All acceptance checks passed.',flush=True)
