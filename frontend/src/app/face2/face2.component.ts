import { Rec } from './rec.model';
import { Component, OnInit } from '@angular/core';
import { ItemsService } from './../services/items.service';

@Component({
	selector: 'app-face2',
	templateUrl: './face2.component.html',
	styleUrls: ['./face2.component.scss']
})
export class Face2Component implements OnInit {
	recs: Rec[];

	constructor(private itemService: ItemsService) {
		this.recs = new Array<Rec>();
		this.recs.push(new Rec("name1","abc1","abcd1","abcde1"));
		this.recs.push(new Rec("name2","abc2","abcd2","abcde2"));
	 }

	ngOnInit() {

	}

	dostuff2() {
		var fileInput = document.getElementById("input1") as HTMLInputElement;
		var files = fileInput.files;

		var xhr = new XMLHttpRequest();
		var result
		xhr.onreadystatechange = () => {
			if (xhr.readyState === 4 && xhr.status === 200) {
				result = xhr.responseText;
				console.log('success!!');
				this.postData(result);
			}
		}

		xhr.open("POST", "https://dev.sighthoundapi.com/v1/detections?type=face,person&faceOption=landmark,gender");
		xhr.setRequestHeader("Content-type", "application/octet-stream");
		xhr.setRequestHeader("X-Access-Token", "fGF1DfdEWCeTaAqAdEsHXY0MMuo92avXuOhL");
		xhr.send(files[0]);
	}// dostuff2 end

	postData(data) {
		let j = JSON.stringify(data);

		this.itemService.postFaceData(j).subscribe(
			(item: any) => {
				if (item != null) {
					
				}
			},
			(error) => console.log(error)
		);
	}

}
