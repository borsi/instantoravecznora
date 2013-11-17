<?php

setlocale(LC_ALL, "UTF-8");

// ez biztosan kiábrándító.
$fonev = array_map('trim', file("./data/fonev.txt"));
$foneve = file("./data/foneve.txt", FILE_IGNORE_NEW_LINES);
$fonevbol = file("./data/fonevbol.txt", FILE_IGNORE_NEW_LINES);
$fonevvel = file("./data/fonevvel.txt", FILE_IGNORE_NEW_LINES);
$jelzo = file("./data/jelzo.txt", FILE_IGNORE_NEW_LINES);
$leg_jelzo = file("./data/legjelzo.txt", FILE_IGNORE_NEW_LINES);
$ige_alanyi = file("./data/ige_alanyi_e3.txt", FILE_IGNORE_NEW_LINES);
$ige_targyas = file("./data/ige_targyas_e3.txt", FILE_IGNORE_NEW_LINES);
$szerkezet = file("./data/szerkezet.txt", FILE_IGNORE_NEW_LINES);

function random_word($kind)
{
    $c = "echo \$GLOBALS[\"$kind\"][array_rand(\$GLOBALS[\"$kind\"])];";
    return trim(eval($c));
}

function oravecz_nora()
{
    global $szerkezet;
    $words = explode(' ', $szerkezet[array_rand($szerkezet)]);
    $ret = "";

    foreach($words as &$w)
    {
        $ww = $w;
        if (preg_match("/{(.+?)}/", $ww, $match))
        {
            $ret .= (random_word($match[1]) . " ");
        }
        else
        {
            $ret .= ($ww . " ");
        }
    }

    return $ret;
}
?>
<head> 
    <link href='http://fonts.googleapis.com/css?family=Just+Me+Again+Down+Here|Great+Vibes|Berkshire+Swash|Sacramento' rel='stylesheet' type='text/css'>
</head>
<div id="header"></div>

<div id="content">
<? php echo oravecz_nora(); ?>
</div>

<div id="footer"></div>
//echo random_word('fonev');


?>
