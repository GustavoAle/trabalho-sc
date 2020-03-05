$fn = 128;


module base(){
    cylinder(h=7.9,d=11.8);
}

module eixo(){
    translate([0,0,-1])
    cylinder(h=10,d=5.6);

}

union(){
    difference(){
        base();
        eixo();
    }

    translate([1.9,-2.5,0])
    cube([1,5,7.9]);
}
