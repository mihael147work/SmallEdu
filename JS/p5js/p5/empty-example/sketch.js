var hintImage, skyImage, stars = [];

let epY = 0;
let epX = 0;
let epZ = 0;
let size = 100;

//let skyImage;
let rhTex;;

function setup() {


createCanvas(windowWidth, windowHeight, WEBGL);
//noCursor();
//noStroke();


//hintImage = loadImage("//bit.ly/hintImage");
skyImage = loadImage("bgsky.jpg");
rhTex = loadImage("bmstu.png");

 
}

function draw() {


background(200,100,100);


//image(skyImage,0,0)
//ellipse(200, 200, 50, 50);

//epZ = mouseY - 200;
//epZ = map(mouseY, 0, -100, 0, height);
epZ = map(mouseY, 100, height, 0, -500);
epX = map(mouseX, 100, 1000, 0, -500);
epY = map(mouseY, 100, 1000, 0, -500);

//plane(50, 50);

rotateX(-mouseX * 0.01);
rotateY(-mouseY * 0.01);
box(50, 50, 50, 3, 3);

renderEggPlanet();


console.log("draw function!");


}



function renderEggPlanet(){

	texture(rhTex);
	translate(epX,epY,epZ);
	//rotateY(radians(mouseX/4));
	rotateZ(radians(-mouseX/4));
	rotateX(radians(-mouseY/4));
	
	sphere(size);

}