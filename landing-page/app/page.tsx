import { promises as fs } from 'fs';
import path from 'path';
import Link from 'next/link';

interface Presentation {
  title: string;
  href: string;
  tags: string[];
}

interface Microsite extends Presentation {
  description: string;
}

export default async function HomePage() {
  const jsonPath = path.join(process.cwd(), 'data', 'presentations.json');
  const fileContents = await fs.readFile(jsonPath, 'utf8');
  const { presentations, microsites }: { presentations: Presentation[]; microsites: Microsite[] } =
    JSON.parse(fileContents);

  const featuredKeywords = ['Preeclampsia', 'Gestational Diabetes', 'Fetal Growth Restriction', 'Twin'];
  const featuredPresentations = presentations
    .filter((p) => featuredKeywords.some((kw) => p.title.includes(kw)))
    .slice(0, 8);

  return (
    <div className="bg-slate-900 text-white min-h-screen font-sans">
      {/* Header */}
      <header className="container mx-auto px-4 py-6 flex justify-between items-center">
        <div className="text-2xl font-bold">
          <span className="text-cyan-400">MFM</span> Presentations
        </div>
        <nav className="flex items-center gap-6">
          <Link href="/library" className="text-slate-400 hover:text-white transition-colors">
            Full Library
          </Link>
          <a
            href="https://github.com/chukwumaonyeije/mfm-presentations"
            target="_blank"
            rel="noopener noreferrer"
            className="text-slate-400 hover:text-white transition-colors"
          >
            GitHub
          </a>
        </nav>
      </header>

      {/* Hero */}
      <section className="container mx-auto px-4 py-20 text-center">
        <h1 className="text-5xl md:text-7xl font-extrabold tracking-tight mb-6 leading-tight">
          The Open-Source Library for{' '}
          <span className="text-cyan-400">Maternal-Fetal Medicine</span>
        </h1>
        <p className="text-lg md:text-xl text-slate-400 max-w-3xl mx-auto mb-10">
          80+ evidence-based clinical presentations and interactive tools for patients, providers,
          and sonographers. Created and maintained by Dr. Chukwuma Onyeije, MD.
        </p>
        <div className="flex flex-wrap justify-center gap-4">
          <Link
            href="/library"
            className="bg-cyan-500 hover:bg-cyan-600 text-white font-bold py-3 px-8 rounded-lg transition-transform transform hover:scale-105"
          >
            Explore the Full Library →
          </Link>
          <a
            href="#microsites"
            className="bg-slate-700 hover:bg-slate-600 text-white font-bold py-3 px-8 rounded-lg transition-transform transform hover:scale-105"
          >
            Interactive Tools
          </a>
        </div>

        <div className="flex flex-wrap justify-center gap-8 mt-16 text-center">
          {[
            { value: '80+', label: 'Presentations' },
            { value: '6', label: 'Interactive Tools' },
            { value: '100%', label: 'Open-Source' },
            { value: 'Free', label: 'Always' },
          ].map((stat) => (
            <div key={stat.label}>
              <div className="text-3xl font-bold text-cyan-400">{stat.value}</div>
              <div className="text-slate-400 text-sm mt-1">{stat.label}</div>
            </div>
          ))}
        </div>
      </section>

      {/* Featured Presentations */}
      <section className="container mx-auto px-4 py-16">
        <h2 className="text-3xl font-bold text-center mb-2">Featured Presentations</h2>
        <p className="text-slate-400 text-center mb-10">Commonly used resources for high-risk obstetric care</p>
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
          {featuredPresentations.map((p, i) => (
            <a
              href={p.href}
              key={i}
              target="_blank"
              rel="noopener noreferrer"
              className="bg-slate-800 p-6 rounded-lg hover:bg-slate-700 border border-slate-700 hover:border-cyan-500 transition-all transform hover:-translate-y-1 flex flex-col"
            >
              <h3 className="font-bold text-base mb-3 text-cyan-400 leading-snug">{p.title}</h3>
              <div className="flex flex-wrap gap-2 mt-auto pt-3">
                {p.tags.slice(0, 2).map((tag) => (
                  <span key={tag} className="bg-slate-700 text-cyan-300 text-xs font-medium px-2.5 py-0.5 rounded-full">
                    {tag}
                  </span>
                ))}
              </div>
            </a>
          ))}
        </div>
        <div className="text-center mt-10">
          <Link href="/library" className="text-cyan-400 hover:text-cyan-300 font-semibold underline underline-offset-4">
            View all {presentations.length} presentations →
          </Link>
        </div>
      </section>

      {/* Microsites */}
      <section id="microsites" className="bg-slate-800/50 py-20">
        <div className="container mx-auto px-4">
          <h2 className="text-3xl font-bold text-center mb-2">Interactive Clinical Tools</h2>
          <p className="text-slate-400 text-center mb-12">Evidence-based calculators and decision-support microsites</p>
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
            {microsites.map((m, i) => (
              <a
                href={m.href}
                key={i}
                target="_blank"
                rel="noopener noreferrer"
                className="bg-slate-800 p-6 rounded-lg hover:bg-slate-700 border border-slate-700 hover:border-cyan-500 transition-all transform hover:-translate-y-1 flex flex-col"
              >
                <h3 className="font-bold text-xl mb-2 text-cyan-400">{m.title}</h3>
                <p className="text-slate-400 flex-grow text-sm leading-relaxed">{m.description}</p>
                <div className="flex flex-wrap gap-2 mt-4">
                  {m.tags.map((tag) => (
                    <span key={tag} className="bg-cyan-900/50 text-cyan-300 text-xs font-medium px-2.5 py-0.5 rounded-full">
                      {tag}
                    </span>
                  ))}
                </div>
              </a>
            ))}
          </div>
        </div>
      </section>

      {/* Footer */}
      <footer className="text-center py-10 text-slate-500 text-sm">
        <p className="mb-1">
          &copy; 2026{' '}
          <a href="https://doctorswhocode.blog/" target="_blank" rel="noopener noreferrer" className="hover:text-slate-300 transition-colors">
            Dr. Chukwuma Onyeije
          </a>
          . All presentations are open-source.
        </p>
        <p>
          <a href="https://github.com/chukwumaonyeije/mfm-presentations" target="_blank" rel="noopener noreferrer" className="hover:text-slate-300 transition-colors">
            View on GitHub
          </a>
        </p>
      </footer>
    </div>
  );
}
