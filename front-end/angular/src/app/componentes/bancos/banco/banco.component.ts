import { Component, OnInit } from '@angular/core';
import { ApiService } from '../../../api.service';

@Component({
  selector: 'app-banco',
  templateUrl: './banco.component.html',
  styleUrls: ['./banco.component.css']
})
export class BancoComponent implements OnInit {
  bancos;

  constructor(private apiService: ApiService) { }
    ngOnInit() {
      this.apiService.getBanco().subscribe((data)=>{
        console.log(data);
        this.bancos = data;
        console.log(this.bancos[0])
      });
}
}
