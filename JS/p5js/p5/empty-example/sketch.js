var hintImage, skyImage, stars = [];

let epY = 0;
let epX = 0;
let epZ = 0;
let size = 70;
let pulse = 70;
let flag = 1;
let check = 10;

let poY = 0;
let poX = 0;

let speed = 0.1;

let krug = 20;
//let skyImage;
let rhTex;;

let life = 1000;

function setup() {


createCanvas(windowWidth, windowHeight, WEBGL);
//noCursor();
//noStroke();


//hintImage = loadImage("//bit.ly/hintImage");
//skyImage = loadImage("bgsky.jpg");
rhTex = loadImage("bmstu.png");

 
}

function draw() {


 background(0, 0, 0);
  noFill();

  // The two parameters of the point() method each specify
  // coordinates.
  // The first parameter is the x-coordinate and the second is the Y
  stroke(255);
  
  poX = map(mouseX + 5, 0, width, 100 - width/2, width/2 - 100);
  poY = map(mouseY + 5, 0, height, 100 - height/2, height/2 - 100);


  point(poX, poY);
  point(0, height * 0.25);

  // Coordinates are used for drawing all shapes, not just points.
  // Parameters for different functions are used for different
  // purposes. For example, the first two parameters to line()
  // specify the coordinates of the first endpoint and the second
  // two parameters specify the second endpoint
  stroke(0, 153, 255);
  line(-0.5 * width, height * 0.06 - (mouseX - width/2) * 0.1 - (mouseY - height/2) * 0.1, 
  	width * 0.5, height * 0.06 + (mouseX - width/2) * 0.1 - (mouseY - height/2) * 0.1);

  // By default, the first two parameters to rect() are the
  // coordinates of the upper-left corner and the second pair
  // is the width and height
  stroke(255, 153, 0);
  rect(width * -0.2 + (mouseX - width/2) * 0.3, height * -0.2 + (mouseY - height/2) * 0.1, width * 0.4, height * 0.4);

//epZ = mouseY - 200;
//epZ = map(mouseY, 0, -100, 0, height);
life = map((width/2-mouseX)*(width/2-mouseX)+(height/2-mouseY)*8*(height/2-mouseY), 0, 2*height*height + width*width/4, 0.001, 2);
//map((width/2-mouseX)*(width/2-mouseX)+(height/2-mouseY)*(height/2-mouseY), 0, height*height + width*width, -200, 1000); 
epZ = 0;
epX = map(mouseX, 0, width, 100 - width/2, width/2 - 100);
epY = map(mouseY, 0, height, 100 - height/2, height/2 - 100);

speed = map((width/2-mouseX)*(width/2-mouseX)+(height/2-mouseY)*(height/2-mouseY)*4, 0, height*height + width*width/4, 0.5, 6);


if (pulse < 500 & flag == 1) {
	pulse = pulse + speed;
	//size = size - speed;
	if (pulse > 499) {
		flag = 0;
	//	console.log("flag = 0");
	}
}

if (pulse > 200 & flag == 0) {
	//console.log("if second begun");
	pulse = pulse - speed;
	//size = size + speed;
	if (pulse < 201) {
		flag = 1;
	//	console.log("flag = 1");
	}
}

krug += 2;
size = pulse/5;

renderEggPlanet();

 point(poX + 200, poY + 200);

console.log(life);
/*background(0, 0, 0);


//image(skyImage,0,0)
//ellipse(200, 200, 50, 50);

//epZ = mouseY - 200;
//epZ = map(mouseY, 0, -100, 0, height);
//epZ = map(mouseY, 100, height, 0, -500);
//epX = map(mouseX, 100, 1000, 0, -500);
//epY = map(mouseY, 100, 1000, 0, -500);


//plane(300, 500, 100, 10);
//check += 0.01;
//rotateX(check);
//rotateY(check);
//box(50, 50, 50, 3, 3);


//makeBox(50,50);

//renderEggPlanet();
console.log("draw function!");

*/
}


function makeBox(bwidth, bheight){

	//translate(check);
	//rotateY(3);
	//rotateX(check);
	box(bwidth, bheight);

}


function renderEggPlanet(){

//	texture(rhTex);
	translate(epX,epY,epZ);
	rotateZ(radians(life*pulse));
	rotateX(radians(life*krug));
	rotateY(radians(krug*life));
	
	sphere(size);

}