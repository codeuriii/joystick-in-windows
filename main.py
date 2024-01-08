
import pygame
from pynput.mouse import Button
from pynput.keyboard import Key
import pynput
import pyautogui
import time
import os

pygame.init()
mouse = pynput.mouse.Controller()
keyboard = pynput.keyboard.Controller()

clicked_a = False
clicked_b = False
clicked_x = False
clicked_y = False
clicked_home = False
clicked_screen = False
clicked_plus = False
clicked_moin = False
clicked_fleche_bas = False
clicked_l = False
clicked_r = False
valid = True
clicked_valid = False

# Initialiser le module joystick
pygame.joystick.init()

# Vérifier le nombre de manettes connectées
joystick_count = pygame.joystick.get_count()
print(f"Nombre de manettes connectées : {joystick_count}")

if joystick_count > 0:
    # Sélectionner la première manette
    joystick = pygame.joystick.Joystick(0)
    joystick.init()

    print(f"Nom de la manette : {joystick.get_name()}")

    try:
        clock = pygame.time.Clock()
        target_fps = 60  # Définir le FPS cible

        while True:
            # Gérer les événements
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

            # Lire les entrées de la manette
            axes = [joystick.get_axis(i) for i in range(joystick.get_numaxes())]
            
            # les boutons seront les clicks de souris
            buttons = [joystick.get_button(i) for i in range(joystick.get_numbuttons())]
            if valid:
                # bouger la souris naturellement
                first_joy_stick = axes[0:2]
                first_dx = round(first_joy_stick[0], 1)
                first_dy = round(first_joy_stick[1], 1)
                mouse.move(first_dx*15, first_dy*15)

                # controller le scroll
                second_joy_stick = axes[2:4]
                second_dx = round(second_joy_stick[0], 1)
                second_dy = -round(second_joy_stick[1], 1)
                mouse.scroll(second_dx*0.25, second_dy*0.25)


                # a -> clique gauche
                a = buttons[0]
                if a == 1:
                    if not clicked_a:
                        mouse.press(Button.left)
                        # print("a press")
                        clicked_a = True
                elif clicked_a:
                    mouse.release(Button.left)
                    # print("a realease")
                    clicked_a = False

                # b -> Echap
                b = buttons[1]
                if b == 1:
                    if not clicked_b:
                        keyboard.press(Key.esc)
                        # print("b press")
                        clicked_b = True
                elif clicked_b:
                    keyboard.release(Key.esc)
                    # print("b realase")
                    clicked_b = False

                # x -> clique gauche et droit
                x = buttons[2]
                if x == 1:
                    if not clicked_x:
                        mouse.press(Button.left)
                        mouse.press(Button.right)
                        # print("x press")
                        clicked_x = True
                elif clicked_x:
                    mouse.release(Button.left)
                    mouse.release(Button.right)
                    # print("x realase")
                    clicked_x = False

                # y -> clique droit
                y = buttons[3]
                if y == 1:
                    if not clicked_y:
                        mouse.press(Button.right)
                        # print("y press")
                        clicked_y = True
                elif clicked_y:
                    mouse.release(Button.right)
                    # print("y realase")
                    clicked_y = False

                # home -> win + D
                home = buttons[5]
                if home == 1:
                    if not clicked_home:
                        keyboard.press(Key.cmd)
                        keyboard.type("d")
                        keyboard.release(Key.cmd)
                        # print("home press")
                        clicked_home = True
                elif clicked_home:
                    # print("home realase")
                    clicked_home = False

                # screen -> imp ecran
                screen = buttons[-1]
                if screen == 1:
                    if not clicked_screen:
                        # Récupérer l'image capturée
                        screenshot = pyautogui.screenshot()

                        screenshot_folder = screenshot_folder = os.path.join(os.path.expanduser("~"), "screenshots")

                        try:
                            os.makedirs(screenshot_folder)
                        except Exception as e:
                            print(e)

                        timestamp = time.strftime("%d-%m-%Y_%H-%M-%S")
                        filename = os.path.join(screenshot_folder, f"Screenshot_{timestamp}.png")

                        # Sauvegarder l'image
                        screenshot.save(filename)
                        # print("screen press")
                        clicked_screen = True
                elif clicked_screen:
                    # print("screen realase")
                    clicked_screen = False

                # + -> volume +
                plus = buttons[6]
                if plus == 1:
                    if not clicked_plus:
                        keyboard.press(Key.media_volume_up)
                        # print("plus press")
                        clicked_plus = True
                elif clicked_plus:
                    keyboard.release(Key.media_volume_up)
                    # print("plus realase")
                    clicked_plus = False

                # - -> volume -
                moin = buttons[4]
                if moin == 1:
                    if not clicked_moin:
                        keyboard.press(Key.media_volume_down)
                        # print("moin press")
                        clicked_moin = True
                elif clicked_moin:
                    keyboard.release(Key.media_volume_down)
                    # print("moin realase")
                    clicked_moin = False

                
                # fleche directionelle -> raccourcis genre alt avec l et r
                
                fleche_bas = buttons[12]
                if fleche_bas == 1:
                    if not clicked_fleche_bas:
                        keyboard.press(Key.alt)
                        keyboard.tap(Key.tab)
                        # print("fleche_bas press")
                        clicked_fleche_bas = True
                elif clicked_fleche_bas:
                    keyboard.release(Key.alt)
                    # print("fleche_bas realase")
                    clicked_fleche_bas = False

                # l et r -> raccourcis
                l = buttons[10]
                if l == 1:
                    if not clicked_l:
                        if clicked_fleche_bas:
                            keyboard.tap(Key.tab)
                        # print("l press")
                        clicked_l = True
                elif clicked_l:
                    # print("l realase")
                    clicked_l = False

                r = buttons[9]
                if r == 1:
                    if not clicked_r:
                        if clicked_fleche_bas:
                            keyboard.press(Key.shift)
                            keyboard.tap(Key.tab)
                            keyboard.release(Key.shift)
                        # print("r press")
                        clicked_r = True
                elif clicked_r:
                    # print("r realase")
                    clicked_r = False

                l = buttons[10]
                if l == 1:
                    if not clicked_l:
                        if clicked_fleche_bas:
                            keyboard.tap(Key.tab)
                        # print("l press")
                        clicked_l = True
                elif clicked_l:
                    # print("l realase")
                    clicked_l = False

            if buttons[7] == buttons[8] == 1:
                clicked_valid = True
            else:
                if clicked_valid:
                    if valid:
                        valid = False
                    else:
                        valid = True
                    clicked_valid = False


            # print(buttons)

            # Réguler le FPS
            clock.tick(target_fps)

    except KeyboardInterrupt:
        pygame.quit()
else:
    print("Aucune manette connectée.")
