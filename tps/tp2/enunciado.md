# TP2


# Enunciado

En algún lugar cerca del Santiago Bernabéu, hay un bote de remos que usaran los hinchas de River y los de Boca para cruzar 
el Rio Manzanares para ir a la cancha. El bote puede contener exactamente cuatro personas y no saldrá de la orilla con más
o menos. Para garantizar la seguridad de los pasajeros, no está permitido poner a un hincha de Boca en el bote con tres de
River ni a uno de River con tres de Boca. Cualquier otra combinación es segura.

Cuando cada hincha que sube al barco, debe invocar una función llamada a_bordo(). Se debe garantizar que los cuatro hinchas
de cada viaje en barco invoquen la función antes de que lo haga cualquiera de los hinchas del siguiente viaje en barco.
Después de que los cuatro hinchas hayan invocado la función, exactamente uno de ellos debería llamar a una función llamada
a_remar(), lo que indica que los hinchas tomarán los remos. No importa qué hincha llame a la función, siempre y cuando solo
uno lo haga.

No te preocupes por la dirección del viaje. Supongamos que solo estamos interesados en el tráfico que va en una de las
direcciones.

