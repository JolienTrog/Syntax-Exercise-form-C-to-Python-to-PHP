using System;

namespace Parkplatz_ohne_Funktion_VS2019
{
    class Program
    {
        static void Main(string[] args)
        {
            // Variablen
            // Array Parkplatz
            int[] Parkplatz = {0, 1, 2, 2, 1, 0, 0, 0, 1, 1};

            while (true)
            {
                // Parkplatzausgabe
                // for Schleife
                for (int i = 0; i < 10; i++)
                {
                    switch (Parkplatz[i])
                    {
                        case 0:
                            Console.WriteLine($"Parkplatz {i + 1} ist frei");
                            break;
                        case 1:
                            Console.WriteLine($"Parkplatz {i + 1} ist belegt");
                            break;
                        case 2:
                            Console.WriteLine($"Parkplatz {i + 1} ist reserviert");
                            break;
                    }
                }

                // Eingabe
                Console.WriteLine("\nGeben Sie den Status an: (0:löschen 1:belegen 2:reservieren)");
                int istatus = Convert.ToInt32(Console.ReadLine());
                Console.WriteLine("Geben Sie die Parkplatz-Nummer an: ");
                int ParkplatzNr = Convert.ToInt32(Console.ReadLine());

                switch (istatus)
                {
                    case 0:
                        Console.WriteLine($"Parkplatz {ParkplatzNr} wurde freigegeben\n\n");
                        Parkplatz[ParkplatzNr - 1] = 0;
                        break;
                    case 1:
                        Console.WriteLine($"Parkplatz {ParkplatzNr} wurde belegt\n\n");
                        Parkplatz[ParkplatzNr - 1] = 1;
                        break;
                    case 2:
                        Console.WriteLine($"Parkplatz {ParkplatzNr} wurde reserviert\n\n");
                        Parkplatz[ParkplatzNr - 1] = 2;
                        break;
                    default:
                        Console.WriteLine("Ungültige Eingabe\n\n");
                        break;
                }
            }
        }
    }
}