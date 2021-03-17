import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders, HttpParams } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class ApiService {

  constructor(private httpClient: HttpClient) { }
//Banco
  public getBanco(){
    return this.httpClient.get(`http://127.0.0.1:5000/banco/banco`);
  }
  public getUmBanco(idbanco:any){
    return this.httpClient.get(`http://127.0.0.1:5000/api/banco/banco${idbanco}`);
  }
  public postBanco(banco:any){
    return this.httpClient.post(`http://127.0.0.1:5000/banco/banco`, banco);
  }
//Cliente
  public getCliente(){
    return this.httpClient.get(`http://127.0.0.1:5000/cliente/clientes`);
  }

  public getUmCliente(id_cliente:any){
    return this.httpClient.get(`http://127.0.0.1:5000/cliente/cliente${id_cliente}`);
  }

  public postCliente(cliente:any){
    return this.httpClient.post(`http://127.0.0.1:5000/cliente/clientes`, cliente,);
  }

  public putCliente(cliente:any){
    return this.httpClient.put(`http://127.0.0.1:5000/cliente/clientes`,cliente);
  }

  public deleteCliente(id_cliente:any){
    return this.httpClient.delete(`http://127.0.0.1:5000/cliente/cliente/${id_cliente}`);
  }

//Imovel
  public getImovel(){
    return this.httpClient.get(`http://127.0.0.1:5000/imovel/imovel`);
  }
//Proprietario
  public getProprietario(){
    return this.httpClient.get(`http://127.0.0.1:5000/proprietario/proprietario`);
  }
//Despesas
  public getDespesas(){
    return this.httpClient.get(`http://127.0.0.1:5000/despesas/despesas`);
  }
}
