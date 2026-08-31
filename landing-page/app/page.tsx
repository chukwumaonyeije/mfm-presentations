import { promises as fs } from 'fs';
import path from 'path';
import Link from 'next/link';
import {
  ArrowRight,
  BookOpen,
  Clock3,
  Code2,
  Github,
  Heart,
  Sparkles,
  Stethoscope,
  Wrench,
} from 'lucide-react';
import PulseLine from './components/PulseLine';

interface Presentation {
  title: string;
  href: string;
  quizHref?: string;
  tags: string[];
  description: string;
}

type Microsite = Presentation;

export default async function HomePage() {
  const jsonPath = path.join(process.cwd(), 'data', 'presentations.json');
  const fileContents = await fs.readFile(jsonPath, 'utf8');
  const { presentations, microsites }: { presentations: Presentation[]; microsites: Microsite[] } =
    JSON.parse(fileContents);

  const presentationCount = presentations.length;
  const micrositeCount = microsites.length;
  const latestPresentation = presentations[0];
  const recentPresentations = presentations.slice(0, 4);
  const curatedSlugs = ['basic-gdm', 'fetal-growth-restriction-patients', 'preeclampsia'];
  const clinicalEssentials = curatedSlugs
    .map((slug) => presentations.find((presentation) => presentation.href.includes(slug)))
    .filter((presentation): presentation is Presentation => presentation !== undefined);

  return (
    <div
      className="landing-shell min-h-screen text-white"
      style={{ fontFamily: "var(--font-inter, 'Inter', sans-serif)" }}
    >
      <header className="relative z-20 container mx-auto flex items-center justify-between px-4 py-6">
        <div
          className="text-2xl font-bold"
          style={{ fontFamily: "var(--font-space-grotesk, 'Space Grotesk', sans-serif)" }}
        >
          <span className="text-white">open</span>
          <span className="text-cyan-400">MFM</span>
        </div>
        <nav className="flex items-center gap-6 text-sm">
          <Link href="/interactive" className="text-slate-400 transition-colors hover:text-white">
            Tools
          </Link>
          <Link href="/library" className="text-slate-400 transition-colors hover:text-white">
            Full Library
          </Link>
          <a
            href="https://github.com/chukwumaonyeije/mfm-presentations"
            target="_blank"
            rel="noopener noreferrer"
            className="flex items-center gap-1.5 text-slate-400 transition-colors hover:text-white"
          >
            <Github className="h-4 w-4" />
            GitHub
          </a>
        </nav>
      </header>

      <section className="relative container mx-auto px-4 pb-18 pt-8 md:pt-12">
        <div
          className="hero-glow pointer-events-none absolute"
          style={{
            top: '14%',
            left: '52%',
          }}
        />
        <PulseLine />

        <div className="relative z-10 grid gap-10 lg:grid-cols-[minmax(0,1.15fr)_minmax(320px,420px)] lg:items-end">
          <div className="text-center lg:text-left">
            <div className="mb-8 flex flex-wrap justify-center gap-3 lg:justify-start">
              <span className="eyebrow-pill">
                <Heart className="h-3.5 w-3.5" />
                Open-Source MFM Education
              </span>
              <span className="eyebrow-pill subtle">
                <Sparkles className="h-3.5 w-3.5" />
                Latest deck pinned from the library feed
              </span>
            </div>

            <h1
              className="relative mb-6 text-5xl font-extrabold leading-tight tracking-tight md:text-7xl"
              style={{ fontFamily: "var(--font-space-grotesk, 'Space Grotesk', sans-serif)" }}
            >
              The Open-Source Library for
              <span className="relative mt-2 block text-cyan-400">
                Maternal-Fetal Medicine
                <span
                  className="absolute inset-0 -z-10 blur-xl"
                  style={{
                    background: 'rgba(34, 211, 238, 0.15)',
                    animation: 'pulse-glow 2.5s ease-in-out infinite',
                  }}
                />
              </span>
            </h1>

            <p
              className="mx-auto mb-4 max-w-2xl text-base text-slate-300 md:text-lg lg:mx-0"
              style={{ fontWeight: 300 }}
            >
              openMFM is the public teaching layer for Maternal-Fetal Medicine: evidence-based slide decks,
              patient education, and clinical tools that stay usable in real care.
            </p>

            <p className="mb-10 text-sm text-slate-500">
              Created by <span className="font-medium text-slate-300">Dr. Chukwuma Onyeije, MD</span>
              {' · '}
              <span className="text-cyan-400">Maternal-Fetal Medicine Specialist</span>
            </p>

            <div className="mb-14 flex flex-wrap justify-center gap-4 lg:justify-start">
              <Link
                href="/library"
                className="btn-glow inline-flex items-center gap-2 rounded-lg bg-cyan-500 px-8 py-3 font-semibold text-white transition-all hover:bg-cyan-600"
                style={{
                  fontFamily: "var(--font-space-grotesk, 'Space Grotesk', sans-serif)",
                  letterSpacing: '0.02em',
                }}
              >
                Explore the full library
                <ArrowRight className="h-4 w-4" />
              </Link>
              <Link
                href="/interactive"
                className="btn-glass inline-flex items-center gap-2 rounded-lg px-8 py-3 font-semibold text-slate-200"
                style={{
                  fontFamily: "var(--font-space-grotesk, 'Space Grotesk', sans-serif)",
                  letterSpacing: '0.02em',
                }}
              >
                Interactive tools
              </Link>
            </div>

            <div className="flex flex-wrap justify-center gap-10 sm:gap-14 lg:justify-start">
              {[
                { icon: BookOpen, value: `${presentationCount}+`, label: 'Presentations' },
                { icon: Wrench, value: String(micrositeCount), label: 'Interactive Tools' },
                { icon: Code2, value: 'Open', label: 'Source Available' },
              ].map((stat) => (
                <div key={stat.label} className="flex flex-col items-center gap-1 lg:items-start">
                  <stat.icon className="mb-1 h-5 w-5 text-cyan-400 opacity-60" />
                  <span
                    className="text-3xl font-bold text-cyan-400 sm:text-4xl"
                    style={{ fontFamily: "var(--font-space-grotesk, 'Space Grotesk', sans-serif)" }}
                  >
                    {stat.value}
                  </span>
                  <span
                    className="text-xs uppercase tracking-widest text-slate-500"
                    style={{ letterSpacing: '0.12em' }}
                  >
                    {stat.label}
                  </span>
                </div>
              ))}
            </div>
          </div>

          <aside className="feature-panel">
            <div className="feature-panel__label">
              <Clock3 className="h-4 w-4" />
              Newest presentation
            </div>
            <h2 className="feature-panel__title">{latestPresentation.title}</h2>
            <p className="feature-panel__description">{latestPresentation.description}</p>
            <div className="mb-6 flex flex-wrap gap-2">
              {latestPresentation.tags.slice(0, 4).map((tag) => (
                <span key={tag} className="chip chip-cyan">
                  {tag}
                </span>
              ))}
            </div>
            <div className="feature-panel__meta">
              <span className="feature-panel__meta-item">
                <Stethoscope className="h-4 w-4" />
                Patient-centered counseling
              </span>
              <span className="feature-panel__meta-item">Feed-driven preview</span>
            </div>
            <div className="feature-panel__actions">
              <a
                href={latestPresentation.href}
                target="_blank"
                rel="noopener noreferrer"
                className="feature-panel__link"
              >
                Open latest deck
                <ArrowRight className="h-4 w-4" />
              </a>
              {latestPresentation.quizHref && (
                <a
                  href={latestPresentation.quizHref}
                  target="_blank"
                  rel="noopener noreferrer"
                  className="feature-panel__link feature-panel__link--quiz"
                >
                  Take 5-question quiz
                  <ArrowRight className="h-4 w-4" />
                </a>
              )}
            </div>
          </aside>
        </div>
      </section>

      <section className="container mx-auto px-4 py-16">
        <div className="mb-10 flex flex-col gap-3 md:flex-row md:items-end md:justify-between">
          <div>
            <h2
              className="text-3xl font-bold"
              style={{ fontFamily: "var(--font-space-grotesk, 'Space Grotesk', sans-serif)" }}
            >
              Latest presentations
            </h2>
            <p className="mt-2 max-w-2xl text-sm text-slate-400">
              The home page pulls its newest previews directly from the top of the shared presentation feed,
              so the latest deck shows up here first.
            </p>
          </div>
          <Link
            href="/library"
            className="inline-flex items-center gap-2 text-sm font-semibold text-cyan-400 hover:text-cyan-300"
          >
            Browse the full archive
            <ArrowRight className="h-4 w-4" />
          </Link>
        </div>
        <div className="grid gap-6 lg:grid-cols-[minmax(0,1.2fr)_minmax(0,0.8fr)]">
          {recentPresentations[0] && (
            <a
              href={recentPresentations[0].href}
              target="_blank"
              rel="noopener noreferrer"
              className="recent-card recent-card--primary card-glow rounded-3xl p-7"
            >
              <div className="mb-5 flex items-center justify-between gap-3">
                <span className="section-kicker">Newest release</span>
                <span className="chip chip-subtle">Preview</span>
              </div>
              <h3 className="mb-4 text-2xl font-bold leading-tight text-white">
                {recentPresentations[0].title}
              </h3>
              <p className="mb-6 max-w-2xl text-sm leading-7 text-slate-300">
                {recentPresentations[0].description}
              </p>
              <div className="mb-6 flex flex-wrap gap-2">
                {recentPresentations[0].tags.slice(0, 4).map((tag) => (
                  <span key={tag} className="chip chip-cyan">
                    {tag}
                  </span>
                ))}
              </div>
              <span className="inline-flex items-center gap-2 text-sm font-semibold text-cyan-300">
                View presentation
                <ArrowRight className="h-4 w-4" />
              </span>
            </a>
          )}
          <div className="grid gap-4">
            {recentPresentations.slice(1).map((presentation, index) => (
              <a
                href={presentation.href}
                key={presentation.href}
                target="_blank"
                rel="noopener noreferrer"
                className="recent-card card-glow rounded-2xl p-5"
              >
                <div className="mb-3 flex items-center justify-between gap-3">
                  <span className="section-kicker">Recent addition {index + 2}</span>
                  <ArrowRight className="h-4 w-4 text-slate-500" />
                </div>
                <h3 className="mb-2 text-lg font-semibold leading-snug text-white">
                  {presentation.title}
                </h3>
                <p className="mb-4 text-sm leading-6 text-slate-400">{presentation.description}</p>
                <div className="flex flex-wrap gap-2">
                  {presentation.tags.slice(0, 3).map((tag) => (
                    <span key={tag} className="chip chip-subtle">
                      {tag}
                    </span>
                  ))}
                </div>
              </a>
            ))}
          </div>
        </div>
      </section>

      <section className="container mx-auto px-4 py-8">
        <div className="mb-10 max-w-2xl">
          <h2
            className="text-3xl font-bold"
            style={{ fontFamily: "var(--font-space-grotesk, 'Space Grotesk', sans-serif)" }}
          >
            Clinical essentials
          </h2>
          <p className="mt-2 text-sm text-slate-400">
            Core resources that clinicians and patients return to most often across diabetes, fetal
            growth, and hypertensive disease.
          </p>
        </div>
        <div className="grid grid-cols-1 gap-6 md:grid-cols-2 xl:grid-cols-3">
          {clinicalEssentials.map((presentation) => (
            <a
              href={presentation.href}
              key={presentation.href}
              target="_blank"
              rel="noopener noreferrer"
              className="card-glow flex flex-col rounded-3xl p-6"
            >
              <div className="mb-4 flex items-center justify-between">
                <span className="section-kicker">Core deck</span>
                <BookOpen className="h-4 w-4 text-cyan-400/70" />
              </div>
              <h3 className="mb-3 text-xl font-bold leading-snug text-cyan-300">
                {presentation.title}
              </h3>
              <p className="flex-grow text-sm leading-7 text-slate-400">
                {presentation.description}
              </p>
              <div className="mt-5 flex flex-wrap gap-2">
                {presentation.tags.slice(0, 3).map((tag) => (
                  <span key={tag} className="chip chip-subtle">
                    {tag}
                  </span>
                ))}
              </div>
            </a>
          ))}
        </div>
      </section>

      <section id="microsites" className="py-20" style={{ background: 'rgba(15, 23, 42, 0.5)' }}>
        <div className="container mx-auto px-4">
          <h2
            className="mb-2 text-center text-3xl font-bold"
            style={{ fontFamily: "var(--font-space-grotesk, 'Space Grotesk', sans-serif)" }}
          >
            Interactive clinical tools
          </h2>
          <p className="mx-auto mb-12 max-w-2xl text-center text-sm text-slate-400">
            Evidence-based calculators and decision-support microsites
          </p>
          <div className="grid grid-cols-1 gap-8 md:grid-cols-2 lg:grid-cols-3">
            {microsites.map((microsite) => (
              <a
                href={microsite.href}
                key={microsite.href}
                target="_blank"
                rel="noopener noreferrer"
                className="card-glow flex flex-col rounded-3xl p-6"
              >
                <div className="mb-4 flex items-center justify-between">
                  <span className="section-kicker">Interactive microsite</span>
                  <Wrench className="h-4 w-4 text-cyan-400/70" />
                </div>
                <h3 className="mb-2 text-xl font-bold text-cyan-400">{microsite.title}</h3>
                <p className="flex-grow text-sm leading-relaxed text-slate-400">
                  {microsite.description}
                </p>
                <div className="mt-4 flex flex-wrap gap-2">
                  {microsite.tags.map((tag) => (
                    <span key={tag} className="chip chip-subtle">
                      {tag}
                    </span>
                  ))}
                </div>
              </a>
            ))}
          </div>
        </div>
      </section>

      <footer className="py-12 text-center text-sm">
        <p className="text-slate-600">
          A{' '}
          <a
            href="https://DoctorsWhoCode.blog"
            target="_blank"
            rel="noopener noreferrer"
            className="text-slate-500 transition-colors hover:text-cyan-400"
          >
            DoctorsWhoCode.blog
          </a>
          {' '}project · built to keep MFM education open, current, and usable
        </p>
        <p className="mt-2">
          <a
            href="https://github.com/chukwumaonyeije/mfm-presentations"
            target="_blank"
            rel="noopener noreferrer"
            className="text-slate-600 transition-colors hover:text-cyan-400"
          >
            View on GitHub
          </a>
        </p>
      </footer>
    </div>
  );
}
