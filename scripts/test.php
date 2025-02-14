<?
$product = "HmYkBwozJw4WNyAAFyB1VUcqOE1JZjUIBis7ABdmbU1GIjEJAyIxTRg=";
$defaultdata = array( "showpassword"=>"no", "bgcolor"=>"#ffffff");
$manipulated = array( "showpassword"=>"yes", "bgcolor"=>"#ffffff");

function xor_encrypt($key, $in) {
    $key = $key;
    $text = $in;
    $outText = '';

    // Iterate through each character
    for($i=0;$i<strlen($text);$i++) {
    $outText .= $text[$i] ^ $key[$i % strlen($key)];
    }

    return $outText;
}

function xorStrings($s1, $s2) {
    $result = '';
    $length = min(strlen($s1), strlen($s2));

    for ($i = 0; $i < $length; $i++) {
        $result .= chr(ord($s1[$i]) ^ ord($s2[$i]));
    }

    return $result;
}

$ciphertext = base64_decode($product);
$plaintext = json_encode($defaultdata);

$key = xorStrings($ciphertext, $plaintext);
echo "Der Schlüssel ist: " . $key . "\n";

$a = json_encode($defaultdata);
$b = base64_encode(xor_encrypt("eDWo", $a));
echo "original: ". $b . "\n";

$a = json_encode($manipulated);
$b = base64_encode(xor_encrypt("eDWo", $a));
echo "new: ". $b . "\n";

?>
