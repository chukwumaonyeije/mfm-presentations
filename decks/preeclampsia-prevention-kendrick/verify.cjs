const puppeteer=require('puppeteer');
const path=require('path');
const fs=require('fs');
const {pathToFileURL}=require('url');
(async()=>{
 const browser=await puppeteer.launch({headless:true,pipe:true,executablePath:puppeteer.executablePath(),timeout:20000});
 const page=await browser.newPage();
 const errors=[];page.on('pageerror',e=>errors.push(String(e)));
 await page.setViewport({width:1440,height:1000});
 await page.goto(pathToFileURL(path.join(__dirname,'index.html')).href,{waitUntil:'load'});
 const count=await page.$$eval('.marpit>section',x=>x.length);
 const layout=[];
 for(let i=1;i<=count;i++){
  await page.select('#chooser',String(i-1));
  const check=await page.evaluate(()=>{const s=document.querySelector('.marpit>section:not([hidden])'),r=s.getBoundingClientRect(),nodes=[...s.querySelectorAll('h1,h2,p,li,summary')];return {slide:s.id,overflows:nodes.filter(x=>{const b=x.getBoundingClientRect();return b.bottom>r.bottom-8||b.right>r.right-8||b.left<r.left}).map(x=>x.textContent.slice(0,70)),scroll:s.scrollHeight,height:s.clientHeight}});
  if(check.overflows.length||check.scroll>check.height+2)layout.push(check);
  if([1,7,14,15,16,23,24,25,26].includes(i))await page.screenshot({path:path.resolve('tmp/pdfs/kendrick/slide-'+i+'.png')});
 }
 await page.select('#chooser','0');await page.click('#next');
 const next=await page.$eval('#counter',x=>x.textContent);
 await page.focus('.marpit>section:not([hidden])');await page.keyboard.press('End');const end=await page.$eval('#counter',x=>x.textContent);
 await page.keyboard.press('Home');const home=await page.$eval('#counter',x=>x.textContent);
 await page.click('#refs');const refs=await page.$eval('#references',x=>({open:x.open,citations:x.querySelectorAll('li').length}));await page.keyboard.press('Escape');
 await page.evaluate(()=>{location.hash='#slide-16'});await new Promise(r=>setTimeout(r,100));const hash=await page.$eval('#counter',x=>x.textContent);
 const localLinks=await page.$$eval('a[href]',nodes=>[...new Set(nodes.map(x=>x.getAttribute('href')).filter(x=>!x.startsWith('http')&&!x.startsWith('#')))]);
 const missing=localLinks.filter(x=>!fs.existsSync(path.resolve(__dirname,x)));
 await page.emulateMediaType('print');await page.evaluate(()=>document.querySelectorAll('details').forEach(x=>x.open=true));
 await page.pdf({path:path.join(__dirname,'resources/presentation.pdf'),printBackground:true,preferCSSPageSize:true});
 await page.emulateMediaType('screen');
 await page.setViewport({width:390,height:844});const mobile=[];
 for(let i=1;i<=count;i++){
  await page.select('#chooser',String(i-1));
  const v=await page.evaluate(()=>{const s=document.querySelector('.marpit>section:not([hidden])');return {slide:s.id,width:s.scrollWidth,client:s.clientWidth,body:document.body.scrollWidth}});
  if(v.width>v.client+1||v.body>391)mobile.push(v);
 }
 await page.select('#chooser','15');await page.screenshot({path:path.resolve('tmp/pdfs/kendrick/mobile.png'),fullPage:true});
 await page.setViewport({width:1440,height:1000});
 const forms={};
 for(const f of ['chart-checklist','audit-worksheet']){
  await page.goto(pathToFileURL(path.join(__dirname,'resources',f+'.html')).href);
  await page.emulateMediaType('print');await page.pdf({path:path.resolve('tmp/pdfs/kendrick/'+f+'-html-print.pdf'),printBackground:true,preferCSSPageSize:true});forms[f]=await page.$$eval('article.page',nodes=>nodes.map(n=>({scroll:n.scrollHeight,client:n.clientHeight})));
 }
 await browser.close();
 const report={slides:count,errors,desktopOverflow:layout,mobileOverflow:mobile,navigation:{next,end,home,hash},references:refs,missingLocalLinks:missing,htmlFormPages:forms};
 fs.writeFileSync(path.join(__dirname,'qa-results.json'),JSON.stringify(report,null,2));console.log(JSON.stringify(report,null,2));
 if(errors.length||layout.length||mobile.length||missing.length)process.exitCode=1;
})().catch(e=>{console.error(e);process.exitCode=1});
