import { Component, OnInit } from '@angular/core';
import { ApiService } from '../../../api.service';

@Component({
  selector: 'app-get-imovel',
  templateUrl: './get-imovel.component.html',
  styleUrls: ['./get-imovel.component.css']
})
export class GetImovelComponent implements OnInit {
  imovels;

  constructor(private apiService: ApiService) { }
    ngOnInit() {
      this.apiService.getImovel().subscribe((data)=>{
        console.log(data);
        this.imovels = data;
        console.log(this.imovels[0])
      });
}
}
