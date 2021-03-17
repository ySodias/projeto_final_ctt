import { Component, OnInit } from '@angular/core';
import { ApiService } from '../../../api.service';

@Component({
  selector: 'app-cliente',
  templateUrl: './cliente.component.html',
  styleUrls: ['./cliente.component.css']
})
export class ClienteComponent implements OnInit {

  clientes;

  constructor(private apiService: ApiService) { }
    ngOnInit() {
      this.getCliente();
    }

      getCliente()
      {
          this.apiService.getCliente().subscribe((data)=>{
          console.log(data);
          this.clientes = data;
          console.log(this.clientes[0])
        });
      }

          deleteCliente(id_cliente: number) {
          this.apiService.deleteCliente(id_cliente).subscribe(() => {
          this.getCliente();
        });
      }
      
}


