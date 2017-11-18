import { Rec } from './rec.model';
import { Component, OnInit } from '@angular/core';
import { ItemsService } from './../services/items.service';
import { WebCamComponent } from 'ack-angular-webcam';
import { Http, Request } from '@angular/http';

@Component({
	selector: 'app-face2',
	templateUrl: './face2.component.html',
	styleUrls: ['./face2.component.scss']
})
export class Face2Component implements OnInit {
	recs: Rec[];
	webcam: WebCamComponent;
	disableCamSend = false;

	constructor(private itemService: ItemsService, private http: Http) {
		this.recs = new Array<Rec>();
	}

	ngOnInit() {

	}

	genImage() {
		this.disableCamSend = true;
		this.webcam.captureAsFormData({ fileName: 'file.jpg' })
			.then(formData => this.postFormData(formData))
			.catch(e => console.error(e));
	}

	postFormData(formData) {
		this.dostuff2('cam', formData.get('file'));
	}

	onCamError(err) { }

	onCamSuccess() { }

	dostuff2(callType, data) {
		this.disableCamSend = true;
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
				// if (item != null) {
				// 	console.log(item);
				// }
				console.log(this.recs);
				this.disableCamSend = false;
			},
			(error) => {
				console.log(error);
				this.recs = [];
				this.disableCamSend = false;
			}
		);
	}

}
