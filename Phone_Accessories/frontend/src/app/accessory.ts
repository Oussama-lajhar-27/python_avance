import { inject, Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class AccessoryService {
  private http = inject(HttpClient);
  private url = 'http://127.0.0.1:8000/accessoires';

  // on precise que le retour est un observable de type any
  getaccessoires() {
    return this.http.get<any>(this.url);
  }
}
