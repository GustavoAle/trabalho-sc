$fn=128;

difference(){

    union(){
        import("./stl/joelho-sup-rasgos-c.stl");

        translate([0,0,-13.5])
        cube([20,23,10],center=true);
    }

/*    translate([30,0,0])
    cube([50,50,50],center=true);*/

    color([0,0,1])
    union(){
        translate([5,5,-22])
        cylinder(h=20,d=4);

        translate([-5,-5,-22])
        cylinder(h=20,d=4);
    }

}
