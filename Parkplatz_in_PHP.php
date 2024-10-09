<?php

$Parkplatz = [0, 1, 2, 2, 1, 0, 0, 0, 1, 1];
function Bereich($eingabe, $unten, $oben)
{
    if (($eingabe >= $unten) && ($eingabe <= $oben)) {
        return true;
    } else {
        return false;
    }
}

while (true) {
    for ($i = 0; $i < 10; $i++) {
        switch ($Parkplatz[$i]) {
            case 0:
                echo "Parkplatz " . ($i + 1) . " ist frei \n";
                break;
            case 1:
                echo "Parkplatz " . ($i + 1) . " ist belegt \n";
                break;
            case 2:
                echo "Parkplatz " . ($i + 1) . " ist reserviert \n";
                break;

        }
    }
    while (true) {
        $istatus = readline("Geben Sie den Status an (0:löschen 1:belegt 2:reserviert): ");

        $valid = Bereich($istatus, 0, 2);
        if ($valid) {
            break;
        } else {
            echo "Falsche Eingabe. \n";
        }

    }
    while (true) {

        $ParkplatzNr = readline("Geben Sie die Parkplatz-Nummer an: ");

        $valid = Bereich($ParkplatzNr, 1, 10);
        if ($valid) {
            break;
        } else {
            echo "Falsche Eingabe. \n";
        }
    }
    switch ($istatus) {
        case 0:
            echo "Parkplatz " . $ParkplatzNr . " wurde freigegeben. \n";
            $Parkplatz[$ParkplatzNr - 1] = 0;
            break;
        case 1:
            echo "Parkplatz " . $ParkplatzNr . " wurde belegt. \n";
            $Parkplatz[$ParkplatzNr - 1] = 1;
            break;
        case 2:
            echo "Parkplatz " . $ParkplatzNr . " wurde reserviert. \n";
            $Parkplatz[$ParkplatzNr - 1] = 2;
            break;
        default:
            echo "Ungültige Eingabe. \n";
            break;
    }
    break;
}