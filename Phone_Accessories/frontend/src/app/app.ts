import { Component, inject, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { AccessoryService } from './accessory';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './app.html',
  styleUrl: './app.scss'
})
export class App implements OnInit {

  // injection du service pour communiquer avec le backend fastapi
  private service = inject(AccessoryService);
  // declaration de la liste qui va contenir les accessoires
  accessoires: any[] = [];

  // cette fonction s'execute une seule fois au demarrage
  ngOnInit() {
    // appel de la fonction getAccessoires depuis le service
    this.service.getaccessoires().subscribe((data: any) => {
      console.log('donnees recues:', data);
      // on remplit notre liste avec les donnees recues du serveur
      this.accessoires = data;
    });
  }
}
