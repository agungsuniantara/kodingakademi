<?php
/**
 * Common utility functions for the application
 */

if (!function_exists('sanitizeString')) {
    /**
     * Sanitize a string input
     * @param string $str The string to sanitize
     * @return string The sanitized string
     */
    function sanitizeString($str) {
        return htmlspecialchars(trim($str), ENT_QUOTES, 'UTF-8');
    }
}
?> 