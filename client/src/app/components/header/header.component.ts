import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { MatDialog, MatDialogRef } from '@angular/material/dialog';
import { ApiService } from 'src/app/services/api.service';
import { cakePost } from 'src/app/services/api.service';
import { SearchResultsComponent } from 'src/app/dialogs/search-results/search-results.component';

@Component({
  selector: 'app-header',
  templateUrl: './header.component.html',
  styleUrls: ['./header.component.scss']
})
export class HeaderComponent implements OnInit {
  public query: string = '';

  constructor(public dialog: MatDialog, private api: ApiService, private router: Router) { }

  ngOnInit(): void {
  }

  search() {
    this.api.search(this.query).subscribe((res: any) => {
      console.log('cupcake search:', res);
      const newDialogRef: MatDialogRef<SearchResultsComponent> = this.dialog.open(SearchResultsComponent, {data: res})
    })

  }

}
