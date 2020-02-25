
$fn = 128;

difference(){
    union(){
        difference(){
            import("./stl/acoplador-joelho-femur-c.stl");
            translate([0,0,19])
            cube([30,30,10],center=true);
        }

        translate([0,0,18])
        cylinder(h=15,d=25,center=true);
    }

    translate([0,0,20])
    union(){

        translate([5,5,-22])
        cylinder(h=30,d=4.5);

        translate([-5,-5,-22])
        cylinder(h=30,d=4.5);

    }
}
