def add_element_gui():
    return '''
            <form method="post" action=\"/addelement\">
                <h1>Add Element</h1>
                <table>
                    <tr>
                        <td>Name:</td>
                        <td><input type="text" id="name"/></td>
                    </tr>
                    <tr>
                        <td>Price:</td>
                        <td><input type="text" id="price"/></td>
                    </tr>
                    <tr>
                        <td>Photo: </td>
                        <td><input type="file" id="photo" accept="image/*"/></td>
                    </tr>
                    <tr>
                        <td>Type: </td>
                        <td>
                            <select>
                                <option value="food">Food</option>
                                <option value="dessert">Dessert</option>
                                <option value="drink">Drink</option>
                            </select>
                        </td>
                    </tr>
                </table>
                <input type="submit" id="addElement" value="Add Element"/>
                <div> <a href="/foodmenu">Food Menu</a><div>
            </form>'''
