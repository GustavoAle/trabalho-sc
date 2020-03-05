include <acoplamento-engrenagem.scad>

module microtrava(){

    rotate([0,0,30])
    translate([2.3,-11,-7.5])
    difference(){
        translate([0,0,10])
        cube([10,10,6.5],center=false);

        translate([-3,4.5,9])
        cube([15,1.5,8]);

        translate([5,5,13])
        rotate([90,0,0])
        cylinder(h=6,d=2.5);
    }
}

module travacorrea(){

    union(){

        /*
        translate([0,1,5.8])
        cylinder(h=8,d=3,center=true);
        */
        difference(){
            difference(){
                union(){
                    translate([0,21.5,5.5])
                    cylinder(h=7,d=46,center=true);


                    microtrava();

                    mirror([1,0,0])
                    microtrava();

                    difference(){
                        translate([0,0,2.5])
                        cube([39,43,1],center=true);

                        mirror([1,0,0])
                        linear_extrude(height=10)
                        polygon(points=[[20,-10],[20,25],[0,25]]);

                        linear_extrude(height=10)
                        polygon(points=[[20,-10],[20,25],[0,25]]);
                    }
                }
                translate([0,27.5,6])
                cube([50,50,10],center=true);

            }
            translate([0,21.5,5.5])
            cylinder(h=11,d=42,center=true);

            translate([12,-15.5,4])
            parafuso();

            translate([-12,-15.5,4])
            parafuso();

            translate([0,0,8])
            cube([3,5,10],center=true);
        }
    }
}

travacorrea();
