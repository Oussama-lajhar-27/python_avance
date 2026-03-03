import { ApplicationConfig, provideZoneChangeDetection } from '@angular/core';
import { provideRouter } from '@angular/router';
import { provideHttpClient } from '@angular/common/http';
import { routes } from './app.routes';

export const appConfig: ApplicationConfig = {
  providers: [
    // configuration de la zone pour les changements
    provideZoneChangeDetection({ eventCoalescing: true }),
    provideRouter(routes),
    // connexion avec fastapi
    provideHttpClient()
  ]
};
