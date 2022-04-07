import picture

picture.new_picture(100,200)

picture.set_outline_color("white")       
picture.set_fill_color("white")           
picture.draw_filled_rectangle(0,0,100,200)

picture.set_outline_color("green")
picture.set_fill_color("green")
picture.draw_filled_square(22,0,56)
picture.draw_filled_rectangle(0,96,100,50)


picture.set_outline_color("darkgreen")
picture.set_fill_color("darkgreen")
picture.draw_filled_rectangle(22,0,56,13)


picture.set_outline_color("cyan")
picture.set_fill_color("cyan")
picture.draw_filled_rectangle(22,56,56,70)
picture.draw_filled_rectangle(0,56,100,40)

picture.set_outline_color("blue")
picture.set_fill_color("blue")
picture.draw_filled_rectangle(22,126,56,64)

picture.set_outline_color("darkgreen")
picture.set_fill_color("darkgreen")
picture.draw_filled_rectangle(32,20,10,5)
picture.draw_filled_rectangle(58,20,10,5)
picture.draw_filled_rectangle(42,25,16,7)
# picture.draw_filled_rectangle(38,35,8,14)
# picture.draw_filled_rectangle(54,35,8,14)

picture.set_outline_color("gray")
picture.set_fill_color("gray")
picture.draw_filled_rectangle(22,190,56,10)
picture.save_picture("zombie.png")

picture.run()

