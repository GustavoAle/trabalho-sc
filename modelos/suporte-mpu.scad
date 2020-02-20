$fn = 128;

module base(){
    cube([22,16,10]);
}

module cylinder_cut(){
    translate([-1,8,-18])
    rotate([0,90,0])
    cylinder(h=24,d=39);
}

module hellerman_cut(){
    translate([8,-2,5])
    cube([6,20,3]);
}

module holes(){

    translate([3.5,3,-7])
    union(){
        translate([0,0,10])
        cylinder(h=8,d=2.5);

        translate([15,0,10])
        cylinder(h=8,d=2.5);
    }
}

difference(){

    base();

    cylinder_cut();
    hellerman_cut();
    holes();
}
