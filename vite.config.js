import fs from 'node:fs';
import path from 'node:path';
import { defineConfig } from 'vite';

function phpPreviewPlugin() {
  return {
    name: 'php-preview',
    configureServer(server) {
      server.middlewares.use((req, res, next) => {
        const pathname = (req.url ?? '/').split('?')[0];

        let filePath = null;
        if (pathname === '/' || pathname === '/index.html') {
          filePath = path.join(process.cwd(), 'index.php');
        } else if (pathname.endsWith('.php')) {
          filePath = path.join(process.cwd(), pathname.slice(1));
        }

        if (!filePath || !fs.existsSync(filePath)) {
          next();
          return;
        }

        const html = fs
          .readFileSync(filePath, 'utf-8')
          .replace(/<\?php[\s\S]*?\?>\s*/g, '');

        res.statusCode = 200;
        res.setHeader('Content-Type', 'text/html; charset=utf-8');
        res.end(html);
      });
    },
  };
}

export default defineConfig({
  server: {
    port: 8000,
    strictPort: true,
    open: '/',
  },
  plugins: [phpPreviewPlugin()],
});
