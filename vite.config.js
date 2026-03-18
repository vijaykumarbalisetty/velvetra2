import react from '@vitejs/plugin-react'
import { defineConfig } from 'vite'
import path from 'path'

// https://vite.dev/config/
export default defineConfig({
    base: '/static/',
    plugins: [
        react(),
    ],
    resolve: {
        alias: {
            "@": path.resolve(__dirname, "./src"),
        },
    },
    build: {
        // Build output goes into velvetra/dist/ — which Django reads as templates + static files
        outDir: 'dist',
    },
    server: {
        port: 5173,
        proxy: {
            // Proxy /api and /media calls to the Django backend during development
            '/api': {
                target: 'http://127.0.0.1:8000',
                changeOrigin: true,
            },
            '/media': {
                target: 'http://127.0.0.1:8000',
                changeOrigin: true,
            }
        }
    }
});