import { Component, OnInit } from '@angular/core';
import { ApiService } from '../../../api.service';


@Component({
  selector: 'app-get-propretario',
  templateUrl: './get-propretario.component.html',
  styleUrls: ['./get-propretario.component.css']
})
export class GetPropretarioComponent implements OnInit {

  proprietarios;

  constructor(private apiService: ApiService) { }
    ngOnInit() {
      this.apiService.getProprietario().subscribe((data)=>{
        console.log(data);
        this.proprietarios = data;
        console.log(this.proprietarios[0])
      });

}
}
