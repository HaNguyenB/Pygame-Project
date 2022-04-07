import picture

picture.new_picture(100,200)

picture.set_outline_color("white")       
picture.set_fill_color("white")           
picture.draw_filled_rectangle(0,0,100,200)

picture.set_outline_color("green")
picture.set_fill_color("green")
picture.draw_filled_rectangle(25,0,50,200)
picture.draw_filled_square(22,0,56)

picture.set_outline_color("darkgreen")
picture.set_fill_color("darkgreen")
picture.draw_filled_rectangle(22,56,56,5)

picture.set_outline_color("mediumseagreen")
picture.set_fill_color("mediumseagreen")
picture.draw_filled_rectangle(25,170,50,5)

picture.set_outline_color("forestgreen")
picture.set_fill_color("forestgreen")
picture.draw_filled_rectangle(25,175,50,15)

picture.set_outline_color("black")
picture.set_fill_color("black")
picture.draw_filled_rectangle(25,190,50,10)
picture.draw_filled_square(32,15,10)
picture.draw_filled_square(58,15,10)
picture.draw_filled_rectangle(42,25,16,18)
picture.draw_filled_rectangle(38,35,8,14)
picture.draw_filled_rectangle(54,35,8,14)

picture.set_outline_color("seagreen")
picture.set_fill_color("seagreen")
picture.draw_filled_square(35,190,10)
picture.draw_filled_square(55,190,10)

picture.save_picture("creeper.png")

picture.run()

