$fn = 128;

module base(){

    difference(){
        cube([25,49,10]);

        translate([12.5,-2,-15])
        rotate([-90,0,0])
        cylinder(h=52,d=39);

    }

}

module holes(){

    translate([0,3,0])
    union(){
        translate([2,0,-7])
        union(){
            translate([0,0,10])
            cylinder(h=8,d=2.5);

            translate([21,0,10])
            cylinder(h=8,d=2.5);
        }

        translate([2,43,-7])
        union(){
            translate([0,0,10])
            cylinder(h=8,d=2.5);

            translate([21,0,10])
            cylinder(h=8,d=2.5);
        }
    }


}

module hellerman_cut(){
    translate([-2,22,5])
    cube([30,6,3]);
}

difference(){

    base();
    holes();
    hellerman_cut();
}

//hellerman_cut();
