import { Component, OnInit } from '@angular/core';
import { ApiService } from '../../../api.service';


@Component({
  selector: 'app-post-banco',
  templateUrl: './post-banco.component.html',
  styleUrls: ['./post-banco.component.css']
})
export class PostBancoComponent implements OnInit {

  constructor(private apiService: ApiService) { }

  ngOnInit(): void {
  }

  insereNovoBanco( nome:string ){
    this.apiService.postBanco({ "nome":nome }).subscribe(data => {
      console.log(data)
    },
    error  => {
    console.log("Error", error);
    });
}

}
