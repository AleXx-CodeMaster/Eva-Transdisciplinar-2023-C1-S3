import PySimpleGUI as sg
import time

def main():
    # Variables iniciales
    posicion = 0
    velocidad = 0
    aceleracion = 0  # Aceleración constante
    detenido = False
    
    # Cambiar el tema de PySimpleGUI
    sg.theme('DarkGreen5')


    # Cargar imagen del auto
    image_path = 'auto1.png'
    auto_image = sg.Image(filename=image_path)
    
    # Configuración de la interfaz gráfica
    layout = [
        [sg.Graph((1200, 400), (0, 0), (800, 400), background_color='white', key='graph')],
        [
            sg.Column([
                [sg.Text('Tiempo:', size=(8, 1), justification='right')],
                [sg.Text('Posición:', size=(8, 1), justification='right')],
                [sg.Text('Velocidad:', size=(8, 1), justification='right')]
            ]),
            sg.Column([
                [sg.Text('0.00 s', size=(8, 1), key='-TIEMPO-')],
                [sg.Text('0.00 m', size=(8, 1), key='-POSICION-')],
                [sg.Text('0.00 m/s', size=(8, 1), key='-VELOCIDAD-')]
            ]),
            sg.VSeperator(),
            sg.Column([
                [sg.Button('Iniciar', size=(9, 1))],
                [sg.Button('Detener', size=(9, 1))],
                [sg.Button('Acelerar', size=(9, 1))],
                [sg.Button('Frenar', size=(9, 1))],
                [sg.Button('Reiniciar', size=(9, 1))]
            ])
        ]
    ]
    
    window = sg.Window('Simulación de Movimiento', layout)
    graph = window['graph']
    
    tiempo_inicial = None
    
    # Bucle principal de la simulación
    while True:
        event, values = window.read(timeout=20)
        if event == sg.WINDOW_CLOSED:
            break
        elif event == 'Iniciar' and not detenido:
            tiempo_inicial = time.time()
            while True:
                event, values = window.read(timeout=20)
                if event == 'Detener':
                    detenido = 0
                    break
                elif event == "Acelerar":
                    aceleracion = 2
                elif event == "Frenar":
                    aceleracion = -1
                elif event == "Reiniciar":
                    tiempo_inicial = time.time()
                    posicion = 0
                    velocidad = 0
                    aceleracion = 0

                tiempo_actual = time.time() - tiempo_inicial
                
                # Cálculo de la posición y la velocidad en función del tiempo
                posicion = velocidad * tiempo_actual + 0.5 * aceleracion * tiempo_actual ** 2
                velocidad = velocidad + aceleracion * tiempo_actual
                
                # Actualizar valores en la interfaz gráfica
                window['-TIEMPO-'].update(f"{tiempo_actual:.2f} s")
                window['-POSICION-'].update(f"{posicion:.2f} m")
                window['-VELOCIDAD-'].update(f"{velocidad:.2f} m/s")
                
                # Dibujo del objeto en la posición calculada
                graph.erase()
                graph.draw_image(filename='auto1.png', location=(posicion, 200))
                
                window.refresh()
        
            window.refresh()
    
    window.close()

if __name__ == '__main__':
    main()


