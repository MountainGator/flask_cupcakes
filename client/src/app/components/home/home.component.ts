import { Component, OnInit } from '@angular/core';
import { MatDialog, MatDialogRef } from '@angular/material/dialog';
import { ApiService } from 'src/app/services/api.service';
import { cakePost } from 'src/app/services/api.service';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.scss']
})
export class HomeComponent implements OnInit {

  constructor(public dialog: MatDialog, private api: ApiService) { }

  public cupcakeList: Array<cakePost> = []
  public cakeData: cakePost = {
    _id:<number> 0, 
    flavor:<string> '', 
    size:<string> '', 
    rating:<number> 0, 
    image:<string> '' 
  }

  ngOnInit(): void {
    const res: any = this.api.getAll().subscribe((res: any) => {
      console.log('api response:', res.data);
      this.cupcakeList = res.data;
      this.cakeData._id = res.data.length + 1;
    })
  }

  handleSubmit() {
    this.cakeData['_id'] += 1;
    try {
      const res:any = this.api.createCupcake(this.cakeData).subscribe((data: any) => {
        console.log('Success! Created Cupcake')
      })
    } catch (e) {
      console.error('error:', e)
    }
  }



}
