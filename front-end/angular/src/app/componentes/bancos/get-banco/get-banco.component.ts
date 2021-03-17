import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { ApiService } from '../../../api.service';

@Component({
  selector: 'app-get-banco',
  templateUrl: './get-banco.component.html',
  styleUrls: ['./get-banco.component.css']
})
export class GetBancoComponent {
  banco:any
  constructor(private activatedRoute: ActivatedRoute, private apiService: ApiService) {
    this.activatedRoute.queryParams.subscribe(params => {
      //console.log(params['id'])
      this.carregaBanco(Number(params['id_banco']))
      });

}
ngOnInit(): void {


}
carregaBanco(idbanco:number){
  console.log(idbanco);
  this.apiService.getUmBanco(idbanco).subscribe(data => {
    this.banco = data[0];
  },
  error  => {
  console.log("Error", error);
  });
}
}
