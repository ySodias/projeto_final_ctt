import { Component, OnInit } from '@angular/core';
import { ApiService } from '../../../api.service';

@Component({
  selector: 'app-get-despesas',
  templateUrl: './get-despesas.component.html',
  styleUrls: ['./get-despesas.component.css']
})
export class GetDespesasComponent implements OnInit {

  despesas;

  constructor(private apiService: ApiService) { }
    ngOnInit() {
      this.apiService.getDespesas().subscribe((data)=>{
        console.log(data);
        this.despesas = data;
        console.log(this.despesas[0])
      });

}
}

