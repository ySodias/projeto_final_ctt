import { Component, OnInit } from '@angular/core';
import { ApiService } from '../../../api.service';

@Component({
  selector: 'app-post-proprietario',
  templateUrl: './post-proprietario.component.html',
  styleUrls: ['./post-proprietario.component.css']
})
export class PostProprietarioComponent implements OnInit {

  constructor(private apiService: ApiService) { }

  ngOnInit(): void {
  }
  insereNovoProprietario(nome:string, data_de_nascimento:string, rg:string, cpf:string, estado_civil:string, profissao:string){



    this.apiService.postCliente({"nome":nome, "data_de_nascimento":data_de_nascimento,'rg':rg, "cpf": cpf, "estado_civil":estado_civil, "profissao":profissao}).subscribe(data => {
      console.log(data)

    },
    error  => {
    console.log("Error", error);
    });
}
}
