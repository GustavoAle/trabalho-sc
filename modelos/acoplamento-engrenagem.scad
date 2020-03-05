$fn = 256;

module base(){
    union(){
        engrenagem();

        cube([39,43,4],center=true);

        translate([0,21.5,0]){
            cylinder(h=4,d=39,center=true);
        }
    }
}

module furo(){
    translate([0,21.5,0])
    cylinder(h=20,d=14,center=true);
}

module engrenagem(){
    translate([0,21.5,5.5])
    cylinder(h=7,d=22,center=true);
}

module parafuso(){
    union(){
        translate([0,0,5.5])
        cylinder(h=10,d=5.6,center=true);
        cylinder(h=5,d=3.5,center=true);
    }
}

module chanfro(){
    translate([0,10,6])
    cube([6,6,8],center=true);
}


//engrenagem();
/*
translate([-10.25,10,-23])
rotate([0,0,180])
import("joelho.stl");

rotate([90,0,0])
*/

module parafusos(){

    translate([0,36.5,0])
    parafuso();

    translate([-15.5,21.5,0])
    parafuso();

    translate([15.5,21.5,0])
    parafuso();

    translate([12,-15.5,0])
    parafuso();

    translate([-12,-15.5,0])
    parafuso();

}

module acoplamento(){

    difference() {
        base();
        furo();

        chanfro();

        parafusos();
    }

}


//encaixe_furado();
//acoplamento();
