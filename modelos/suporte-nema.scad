$fn = 128;

module nema(){
    translate([-1,7,-2])
    color([0,0,1])
    cube([40,43,45]);
}

module base_corpo(){

    cube([22,57,47]);

}

module parafuso(){
    translate([11,-6.5,-2])
    union(){
        translate([0,0,-20])
        cylinder(h=50,d=4.5);
        translate([0,0,10])
        cylinder(h=20,d=8);
    }
}

module encaixe(){
    //translate([0,-1,1])
    union(){
        translate([0,0,-0.1])
        polyhedron(points=[ [0,-13,10],
                            [0,0,10],
                            [22,0,10],
                            [22,-13,10],
                            [0,0,25],
                            [22,0,25]],
                    faces=[
                            [0,4,1],//side
                            [1,4,5,2],//back
                            [2,5,3], //side
                            [3,5,4,0],//front
                            [2,3,0,1] //bottom
                            ]);//side
        translate([0,-13,0])
        cube([22,15,10]);
    }
}

module encaixe_furado(){
    difference(){
        encaixe();
        parafuso();
    }
}

module suporte_corpo(){
    difference(){
        base_corpo();
        nema();
    }

    encaixe_furado();

    translate([0,57,0])
    mirror([0,1,0])
    encaixe_furado();
}


module hellerman_cut(){
    translate([-2,7,-8])
    cube([30,6,3]);
}

//hellerman_cut();

module base(){
    difference(){
        translate([0,-13,-23])
        cube([22,83,20]);

        translate([0,70,0])
        parafuso();

        parafuso();

        translate([11,-6.5,-16]) //porca
        cylinder(h=10,d=8);

        translate([11,63.5,-16]) //porca
        cylinder(h=10,d=8);

        //perna
        translate([11,-20,-24])
        rotate([-90,0,0])
        cylinder(h=100,d=30);

        hellerman_cut();

        translate([0,36,0])
        hellerman_cut();

    }
}

//rotate([0,180,0])
suporte_corpo();

//rotate([0,180,0])
base();
