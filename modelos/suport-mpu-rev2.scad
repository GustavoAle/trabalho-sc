$fn = 128;

module base(){
        translate([-2,0,0])
        cube([24,16,5]);
}

module cylinder_cut(){
    translate([-26,8,-2])
    cylinder(h=30,d=39);
}

module hellerman_cut(){
    translate([-5,-2,3])
    cube([3,20,6]);
}

module holes(){

    translate([3.5,3,-12])
    union(){
        translate([0,0,10])
        cylinder(h=8,d=2.5);

        translate([15,0,10])
        cylinder(h=8,d=2.5);
    }
}

module base_furada(){
    difference(){

        base();
        holes();
    }
}

module acoplador(){

    difference(){
        translate([-10,0,0])
        cube([10,16,12]);

        hellerman_cut();

        cylinder_cut();
    }

}

acoplador();

base_furada();
