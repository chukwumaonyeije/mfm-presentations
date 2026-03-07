import { promises as fs } from 'fs';
import path from 'path';
import Link from 'next/link';
import { BookOpen, Wrench, Code2, Github, Heart } from 'lucide-react';
import PulseLine from './components/PulseLine';

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
    <div className="min-h-screen text-white" style={{ fontFamily: "var(--font-inter, 'Inter', sans-serif)" }}>

      {/* ── HEADER ── */}
      <header className="relative z-20 container mx-auto px-4 py-6 flex justify-between items-center">
        <div className="text-2xl font-bold" style={{ fontFamily: "var(--font-space-grotesk, 'Space Grotesk', sans-serif)" }}>
          <span className="text-white">open</span>
          <span className="text-cyan-400">MFM</span>
        </div>
        <nav className="flex items-center gap-6 text-sm">
          <Link href="/library" className="text-slate-400 hover:text-white transition-colors">
            Full Library
          </Link>
          <a
            href="https://github.com/chukwumaonyeije/mfm-presentations"
            target="_blank"
            rel="noopener noreferrer"
            className="text-slate-400 hover:text-white transition-colors flex items-center gap-1.5"
          >
            <Github className="w-4 h-4" />
            GitHub
          </a>
        </nav>
      </header>

      {/* ── HERO ── */}
      <section className="relative container mx-auto px-4 pt-12 pb-20 text-center">
        {/* Radial glow */}
        <div
          className="absolute pointer-events-none"
          style={{
            top: '30%',
            left: '50%',
            transform: 'translate(-50%, -50%)',
            width: '800px',
            height: '600px',
            background: 'radial-gradient(ellipse, rgba(34, 211, 238, 0.06) 0%, transparent 70%)',
          }}
        />

        {/* Pulse line */}
        <PulseLine />

        {/* Badge */}
        <div className="relative z-10 mb-8">
          <span
            className="inline-flex items-center gap-2 px-4 py-1.5 rounded-full text-xs font-medium tracking-widest uppercase"
            style={{
              background: 'rgba(34, 211, 238, 0.08)',
              border: '1px solid rgba(34, 211, 238, 0.2)',
              color: '#22d3ee',
              letterSpacing: '0.15em',
            }}
          >
            <Heart className="w-3 h-3" />
            Open-Source MFM Education
          </span>
        </div>

        {/* Headline */}
        <h1
          className="relative z-10 text-5xl md:text-7xl font-extrabold tracking-tight mb-6 leading-tight"
          style={{ fontFamily: "var(--font-space-grotesk, 'Space Grotesk', sans-serif)" }}
        >
          The Open-Source Library for{' '}
          <span className="relative inline-block">
            <span className="text-cyan-400">Maternal-Fetal Medicine</span>
            <span
              className="absolute inset-0 blur-xl -z-10"
              style={{ background: 'rgba(34, 211, 238, 0.15)', animation: 'pulse-glow 2.5s ease-in-out infinite' }}
            />
          </span>
        </h1>

        {/* Subtitle */}
        <p className="relative z-10 text-base md:text-lg text-slate-400 max-w-2xl mx-auto mb-4" style={{ fontWeight: 300 }}>
          80+ evidence-based clinical presentations and interactive tools for patients, providers,
          and sonographers.
        </p>

        {/* Author */}
        <p className="relative z-10 text-sm text-slate-500 mb-10">
          Created by{' '}
          <span className="text-slate-300 font-medium">Dr. Chukwuma Onyeije, MD</span>
          {' · '}
          <span className="text-cyan-400">Maternal-Fetal Medicine Specialist</span>
        </p>

        {/* CTA Buttons */}
        <div className="relative z-10 flex flex-wrap justify-center gap-4 mb-14">
          <Link
            href="/library"
            className="btn-glow inline-flex items-center gap-2 bg-cyan-500 hover:bg-cyan-600 text-white font-semibold py-3 px-8 rounded-lg transition-all"
            style={{ fontFamily: "var(--font-space-grotesk, 'Space Grotesk', sans-serif)", letterSpacing: '0.02em' }}
          >
            Explore the Full Library →
          </Link>
          <a
            href="#microsites"
            className="btn-glass inline-flex items-center gap-2 text-slate-200 font-semibold py-3 px-8 rounded-lg"
            style={{ fontFamily: "var(--font-space-grotesk, 'Space Grotesk', sans-serif)", letterSpacing: '0.02em' }}
          >
            Interactive Tools
          </a>
        </div>

        {/* Stats */}
        <div className="relative z-10 flex flex-wrap justify-center gap-10 sm:gap-14">
          {[
            { icon: BookOpen, value: '80+', label: 'Presentations' },
            { icon: Wrench, value: '6', label: 'Interactive Tools' },
            { icon: Code2, value: '100%', label: 'Open-Source' },
          ].map((stat) => (
            <div key={stat.label} className="flex flex-col items-center gap-1">
              <stat.icon className="w-5 h-5 mb-1 text-cyan-400 opacity-60" />
              <span
                className="text-3xl sm:text-4xl font-bold text-cyan-400"
                style={{ fontFamily: "var(--font-space-grotesk, 'Space Grotesk', sans-serif)" }}
              >
                {stat.value}
              </span>
              <span className="text-xs uppercase tracking-widest text-slate-500" style={{ letterSpacing: '0.12em' }}>
                {stat.label}
              </span>
            </div>
          ))}
        </div>
      </section>

      {/* ── FEATURED PRESENTATIONS ── */}
      <section className="container mx-auto px-4 py-16">
        <h2
          className="text-3xl font-bold text-center mb-2"
          style={{ fontFamily: "var(--font-space-grotesk, 'Space Grotesk', sans-serif)" }}
        >
          Featured Presentations
        </h2>
        <p className="text-slate-400 text-center mb-10 text-sm">
          Commonly used resources for high-risk obstetric care
        </p>
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
          {featuredPresentations.map((p, i) => (
            <a
              href={p.href}
              key={i}
              target="_blank"
              rel="noopener noreferrer"
              className="card-glow p-6 rounded-lg flex flex-col"
            >
              <h3 className="font-bold text-base mb-3 text-cyan-400 leading-snug">{p.title}</h3>
              <div className="flex flex-wrap gap-2 mt-auto pt-3">
                {p.tags.slice(0, 2).map((tag) => (
                  <span
                    key={tag}
                    className="text-xs font-medium px-2.5 py-0.5 rounded-full"
                    style={{ background: 'rgba(34, 211, 238, 0.1)', color: '#67e8f9' }}
                  >
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

      {/* ── MICROSITES ── */}
      <section id="microsites" className="py-20" style={{ background: 'rgba(15, 23, 42, 0.5)' }}>
        <div className="container mx-auto px-4">
          <h2
            className="text-3xl font-bold text-center mb-2"
            style={{ fontFamily: "var(--font-space-grotesk, 'Space Grotesk', sans-serif)" }}
          >
            Interactive Clinical Tools
          </h2>
          <p className="text-slate-400 text-center mb-12 text-sm">
            Evidence-based calculators and decision-support microsites
          </p>
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
            {microsites.map((m, i) => (
              <a
                href={m.href}
                key={i}
                target="_blank"
                rel="noopener noreferrer"
                className="card-glow p-6 rounded-lg flex flex-col"
              >
                <h3 className="font-bold text-xl mb-2 text-cyan-400">{m.title}</h3>
                <p className="text-slate-400 flex-grow text-sm leading-relaxed">{m.description}</p>
                <div className="flex flex-wrap gap-2 mt-4">
                  {m.tags.map((tag) => (
                    <span
                      key={tag}
                      className="text-xs font-medium px-2.5 py-0.5 rounded-full"
                      style={{ background: 'rgba(34, 211, 238, 0.1)', color: '#67e8f9' }}
                    >
                      {tag}
                    </span>
                  ))}
                </div>
              </a>
            ))}
          </div>
        </div>
      </section>

      {/* ── FOOTER ── */}
      <footer className="text-center py-12 text-sm">
        <p className="text-slate-600">
          A{' '}
          <a
            href="https://DoctorsWhoCode.blog"
            target="_blank"
            rel="noopener noreferrer"
            className="text-slate-500 hover:text-cyan-400 transition-colors"
          >
            DoctorsWhoCode.blog
          </a>
          {' '}project · Open-source under MIT License
        </p>
        <p className="mt-2">
          <a
            href="https://github.com/chukwumaonyeije/mfm-presentations"
            target="_blank"
            rel="noopener noreferrer"
            className="text-slate-600 hover:text-cyan-400 transition-colors"
          >
            View on GitHub
          </a>
        </p>
      </footer>
    </div>
  );
}
