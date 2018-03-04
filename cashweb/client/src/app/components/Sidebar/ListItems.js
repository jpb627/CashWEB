// REACT MODULES ==================================
import React from 'react';
import PropTypes from 'prop-types';

import { NavLink } from 'react-router-dom';
import { Menu, Dropdown, Icon } from 'semantic-ui-react';


const BookMenuItem = (props) => (
    <Menu.Item
        name={props.title}
        as = {NavLink}
        to={`/book/${props.id}`}
        activeClassName="active">
        {props.title}
    </Menu.Item>
);

const MenuItem = () => (
    <h1>HI</h1>
);

const MenuWithSubItem = () => (
    <Dropdown item text='More'>
        <Dropdown.Menu>
            <Dropdown.Item icon='edit' text='Edit Profile'/>
            <Dropdown.Item icon='globe' text='Choose Language'/>
            <Dropdown.Item icon='settings' text='Account Settings'/>
        </Dropdown.Menu>
    </Dropdown>
);

MenuItem.protoTypes = {
    to: PropTypes.string,
    name: PropTypes.string
};

export { BookMenuItem, MenuItem, MenuWithSubItem };
