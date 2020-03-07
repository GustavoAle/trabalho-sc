$fn = 128;

module base(){
    difference(){
        cylinder(h=1.2,d=25);
        translate([0,0,-1])
        cylinder(h=5,d=6);
    }
}

base();
