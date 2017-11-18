import { Rec } from './rec.model';
import { Component, OnInit } from '@angular/core';
import { ItemsService } from './../services/items.service';
import { WebCamComponent } from 'ack-angular-webcam';
import { Http, Request } from '@angular/http';
import { element } from 'protractor';

@Component({
	selector: 'app-face2',
	templateUrl: './face2.component.html',
	styleUrls: ['./face2.component.scss']
})
export class Face2Component implements OnInit {
	recs: Rec[];
	webcam: WebCamComponent;
	disableCamSend = false;
	fcountour : string;

	constructor(private itemService: ItemsService, private http: Http) {
		this.recs = new Array<Rec>();
	}

	ngOnInit() {

	}

	gotoRec() {
		var e = document.getElementById("rec-card");
		e.scrollIntoView(true)
	}

	genImage() {
		this.disableAndClear()
		this.webcam.captureAsFormData({ fileName: 'file.jpg' })
			.then(formData => this.postFormData(formData))
			.catch(e => console.error(e));
	}

	postFormData(formData) {
		this.dostuff2('cam', formData.get('file'));
	}

	onCamError(err) { }

	onCamSuccess() { }

	disableAndClear() {
		this.disableCamSend = true;
		this.recs = [];
		this.fcountour = "";
	}

	dostuff2(callType, data) {
		this.disableAndClear();
		var files;
		var file;
		if (callType === 'cam') {
			file = data;
		} else {
			var fileInput = document.getElementById(data) as HTMLInputElement;
			files = fileInput.files;
			file = files[0];
		}

		var xhr = new XMLHttpRequest();
		var result
		xhr.onreadystatechange = () => {
			if (xhr.readyState === 4 && xhr.status === 200) {
				result = xhr.responseText;
				console.log('success!!');
				this.postData(result);
			}
			else if (xhr.readyState === 4 && xhr.status !== 200) {
				this.disableCamSend = false;
			}
		}

		xhr.open("POST", "https://dev.sighthoundapi.com/v1/detections?type=face,person&faceOption=landmark,gender");
		xhr.setRequestHeader("Content-type", "application/octet-stream");
		xhr.setRequestHeader("X-Access-Token", "fGF1DfdEWCeTaAqAdEsHXY0MMuo92avXuOhL");
		xhr.send(file);
	}// dostuff2 end

	postData(data) {
		let j = JSON.stringify(data);

		this.itemService.postFaceData(j).subscribe(
			(item: any) => {
				this.recs = item.data;
				console.log(item.facecountour)
				// if (item != null) {
				// 	console.log(item);
				// }
				this.fcountour = "../assets/"+item.facecountour;
				console.log(this.recs);				
				this.disableCamSend = false;				
			},
			(error) => {
				console.log(error);
				this.disableAndClear();
			}
		);
	}

}
