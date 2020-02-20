module travacorrea(){

    union(){

        translate([0,10,5.8])
        cylinder(h=8,d=3,center=true);

        difference(){
            difference(){
                union(){
                    translate([0,21.5,5.5])
                    cylinder(h=7,d=26,center=true);


                    difference(){
                        translate([0,0,2.5])
                        cube([39,43,1],center=true);

                        mirror([1,0,0])
                        linear_extrude(height=10)
                        polygon(points=[[20,0],[20,25],[10,25]]);

                        linear_extrude(height=10)
                        polygon(points=[[20,0],[20,25],[10,25]]);
                    }
                }
                translate([0,33,6])
                cube([30,30,10],center=true);

            }
            translate([0,21.5,5.5])
            cylinder(h=11,d=23.5,center=true);

            translate([12,-15.5,4])
            parafuso();

            translate([-12,-15.5,4])
            parafuso();

        }
    }
}
