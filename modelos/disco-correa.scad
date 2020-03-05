include <acoplamento-engrenagem.scad>
include <trava-correa.scad>

module encaixe(){

    difference(){
        union(){

            translate([0,10,5.8])
            cube([5.5,5.5,7],center=true);

            difference(){
                union(){
                    /*centro*/
                    translate([0,21.5,5.8])
                    cylinder(h=7,d=40,center=true);

                    /*saia*/
                    translate([0,21.5,2.3])
                    cylinder(h=0.6,d=46,center=true);
                }
                /*furo*/
                translate([0,21.5,5.8])
                cylinder(h=8,d=22.5,center=true);
            }

        }

        translate([0,2,6.1])
        cube([5.5,5.5,7],center=true);
    }

}

module encaixe_furado(){
    difference(){
        encaixe();
        translate([0,0,3])
        parafusos();
    }
}

encaixe_furado();
/*
color([1,0,0])
acoplamento();

translate([0,0,-0.1])
color([0,1,1])
travacorrea();*/
