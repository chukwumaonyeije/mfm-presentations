'use client';

import { useEffect, useRef } from 'react';

export default function PulseLine() {
  const canvasRef = useRef<HTMLCanvasElement>(null);

  useEffect(() => {
    const canvas = canvasRef.current;
    if (!canvas) return;
    const ctx = canvas.getContext('2d');
    if (!ctx) return;

    let animationId: number;
    let offset = 0;

    const resize = () => {
      canvas.width = window.innerWidth;
      canvas.height = 120;
    };

    const drawPulse = () => {
      if (!ctx || !canvas) return;
      ctx.clearRect(0, 0, canvas.width, canvas.height);

      const midY = canvas.height / 2;
      const segmentWidth = 320;

      offset += 0.6;
      if (offset > segmentWidth) offset -= segmentWidth;

      ctx.beginPath();
      ctx.strokeStyle = 'rgba(34, 211, 238, 0.3)';
      ctx.lineWidth = 2;
      ctx.lineJoin = 'round';
      ctx.lineCap = 'round';

      for (let x = -segmentWidth + offset; x < canvas.width + segmentWidth; x++) {
        const localX = ((x % segmentWidth) + segmentWidth) % segmentWidth;
        const t = localX / segmentWidth;
        let y = midY;

        if (t < 0.35 || t > 0.75) y = midY;
        else if (t >= 0.35 && t < 0.42) y = midY - Math.sin(((t - 0.35) / 0.07) * Math.PI) * 8;
        else if (t >= 0.42 && t < 0.45) y = midY;
        else if (t >= 0.45 && t < 0.48) y = midY + Math.sin(((t - 0.45) / 0.03) * Math.PI * 0.5) * 6;
        else if (t >= 0.48 && t < 0.52) y = midY - Math.sin(((t - 0.48) / 0.04) * Math.PI) * 45;
        else if (t >= 0.52 && t < 0.56) y = midY + Math.sin(((t - 0.52) / 0.04) * Math.PI * 0.5) * 12;
        else if (t >= 0.56 && t < 0.60) y = midY;
        else if (t >= 0.60 && t < 0.72) y = midY - Math.sin(((t - 0.60) / 0.12) * Math.PI) * 14;

        if (x === -segmentWidth + offset) ctx.moveTo(x, y);
        else ctx.lineTo(x, y);
      }
      ctx.stroke();

      const glowX = ((offset % segmentWidth) / segmentWidth) * canvas.width;
      const gradient = ctx.createRadialGradient(glowX, midY, 0, glowX, midY, 60);
      gradient.addColorStop(0, 'rgba(34, 211, 238, 0.2)');
      gradient.addColorStop(1, 'rgba(34, 211, 238, 0)');
      ctx.fillStyle = gradient;
      ctx.fillRect(glowX - 60, midY - 60, 120, 120);

      animationId = requestAnimationFrame(drawPulse);
    };

    resize();
    drawPulse();
    window.addEventListener('resize', resize);

    return () => {
      cancelAnimationFrame(animationId);
      window.removeEventListener('resize', resize);
    };
  }, []);

  return (
    <canvas
      ref={canvasRef}
      className="absolute left-0 w-full pointer-events-none"
      style={{ top: '50%', transform: 'translateY(-50%)', opacity: 0.7 }}
    />
  );
}
