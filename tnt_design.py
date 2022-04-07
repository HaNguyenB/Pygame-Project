import picture

picture.new_picture(90,90)

picture.set_outline_color("crimson")       
picture.set_fill_color("crimson")           
picture.draw_filled_square(0,0,90)

picture.set_outline_color("silver")
picture.set_fill_color("silver")
picture.draw_filled_rectangle(0,30,90,30)

picture.set_outline_color("black")
picture.set_fill_color("black")
picture.draw_filled_rectangle(12,30,18,6)
picture.draw_filled_rectangle(18,30,6,30)
picture.draw_filled_rectangle(33,30,6,30)
picture.draw_filled_rectangle(39,36,6,6)
picture.draw_filled_rectangle(45,42,6,6)
picture.draw_filled_rectangle(51,30,6,30)
picture.draw_filled_rectangle(60,30,18,6)
picture.draw_filled_rectangle(66,30,6,30)

picture.save_picture("tnt.png")
picture.run()