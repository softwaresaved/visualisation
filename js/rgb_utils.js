/**
 * RGB utilities.

 * Copyright (c) 2016-2018, The University of Edinburgh.
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 */

/**
 * Given RGB component values, calculate hex value.
 *
 * @param {integer} r - red
 * @param {integer} g - green
 * @param {integer} b - blue
 * @return {string} hex value.
 */
function rgb_to_hex(r, g, b)
{
    return "#" +
        ("0" + parseInt(r).toString(16)).slice(-2) +
        ("0" + parseInt(g).toString(16)).slice(-2) +
        ("0" + parseInt(b).toString(16)).slice(-2);
}

/**
 * Assuming an RGB component's values are divided into N 
 * chunks from MIN..255 return the colour corresponding
 * to the Ith chunk i.e. MIN + (I * ((255 - MIN) / N))
 *
 * @param {integer} min - minimum RGB component value.
 * @param {integer} i - ith chunk
 * @param {float} n - number of chunks
 * @return {integer} colour component value.
 */
function get_rgb_component(min, i, n)
{
    scale = (255 - min) / n;
    return parseInt(min + (i * scale));
}
