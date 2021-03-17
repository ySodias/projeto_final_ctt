import { Component, OnInit } from '@angular/core';
import { ApiService } from '../../../api.service';

@Component({
  selector: 'app-post-cliente',
  templateUrl: './post-cliente.component.html',
  styleUrls: ['./post-cliente.component.css']
})
export class PostClienteComponent implements OnInit {
  constructor(private apiService: ApiService) { }

  ngOnInit(): void {
  }

  insereNovoCliente(id_banco:string, nome:string, data_de_nascimento:string, rg:string, cpf:string, estado_civil:string, profissao:string, tipo_residencia:string, cep:string, rua:string, numero:string, cidade:string, estado:string, uf:string){



    this.apiService.postCliente({ "id_banco":id_banco, "nome":nome, "data_de_nascimento":data_de_nascimento,'rg':rg, "cpf": cpf, "estado_civil":estado_civil, "profissao":profissao,"tipo_residencia":tipo_residencia, "cep":cep, "rua":rua, "numero":numero, "cidade":cidade, "estado":estado, "uf":uf  }).subscribe(data => {
      console.log(data)

    },
    error  => {
    console.log("Error", error);
    });
}

}
